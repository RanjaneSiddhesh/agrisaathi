import os
import glob
import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)          # remove extra spaces
    text = re.sub(r'[^\u0900-\u097F a-zA-Z0-9.,%-]', '', text)  # keep Marathi + Eng
    return text.strip()



def load_all_pdf_texts_from_folder(folder_path="Data/maharashtra_pdfs"):
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    docs = []

    for pdf in pdf_files:
        print(f"📄 Reading: {pdf}")
        text = ""
        doc = fitz.open(pdf)
        for page in doc:
            text += page.get_text()
        doc.close()

        if len(text.strip()) > 200:
            docs.append(Document(
                page_content=text,
                metadata={"source": os.path.basename(pdf)}
            ))

    return docs


def initialize_vector_store(docs, persist_directory="chroma_db"):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

    if os.path.exists(persist_directory):
        print("⚡ Loading existing Chroma DB...")
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )

    print("⚡ Creating new Chroma DB...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=150)
    chunks = splitter.split_documents(docs)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    db.persist()
    return db
