import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"


def call_together(prompt):
    url = "https://api.together.xyz/v1/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.2,
        "stop": ["</s>"]
    }

    r = requests.post(url, json=payload, headers=headers, timeout=60)
    return r.json()["choices"][0]["text"]


def ask_rag(db, question, language):
    docs = db.similarity_search(question, k=4)
    context = "\n\n".join(d.page_content for d in docs)
#- Answer only in {language}
# #- Use only the CONTEXT
# - If not found say:
#   Marathi: "माहिती उपलब्ध नाही."
#   English: "Not found in dataset."
# - Use bullet points
# - 5 to 8 lines max
    prompt = f"""
You are AgriSaathi AI for Maharashtra farmers.

RULES:

LANGUAGE RULE (VERY STRICT):
- If language is Marathi → answer ONLY in Marathi (Devanagari script).
- If language is English → answer ONLY in English.
- Do NOT mix languages.
- Do NOT transliterate.
-answer in brief.



FORMAT:
- Use bullet points only
- 4 to 6 bullets
- Each bullet max 1 sentence
- No repetition


CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    return call_together(prompt)

