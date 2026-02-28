# 🌾 AgriSaathi: AI-Powered Farmer Assistance System

## 📌 Project Overview
AgriSaathi is an AI-driven agricultural assistance platform designed to help farmers with crop recommendations, disease guidance, and agricultural queries.  

The system leverages Retrieval-Augmented Generation (RAG), Machine Learning models, and Prompt Engineering to deliver region-specific and data-driven responses. It retrieves relevant agricultural knowledge from structured datasets and documents to provide accurate and context-aware answers.

---

## 🚀 Features

- 🌱 AI-based Crop Recommendation System
- 🦠 Disease Prediction & Guidance
- 🤖 Multilingual Chatbot (Marathi, Hindi, English)
- 📚 Retrieval-Augmented Generation (RAG) for accurate answers
- 🧠 Prompt-Engineered LLM Response System
- 🛒 Marketplace Module for farmers
- 🌍 Web-based interactive interface

---

## 🏗️ Tech Stack

- **Programming:** Python  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning:** Scikit-learn  
- **LLM & NLP:** HuggingFace Embeddings, LangChain  
- **Vector Database:** ChromaDB  
- **Tools:** Git, Docker (Basics)

---

## ⚙️ Installation

Follow the steps below to run the project locally.

### STEP 1 – Create Virtual Environment
```bash
pip install virtualenv
virtualenv env
.\env\Scripts\activate
```

---

### STEP 2 – Clone the Repository
```bash
git clone https://github.com/yourusername/AgriSaathi.git
cd AgriSaathi
```

---

### STEP 3 – Install Dependencies
```bash
pip install -r requirements.txt
```

---

### STEP 4 – Run the Flask Application
```bash
python app.py
```

---

### STEP 5 – Open Browser
Navigate to:

```
http://127.0.0.1:5000
```

---

## 🧠 System Workflow

1. User enters agricultural query.
2. Query is processed using NLP techniques.
3. Relevant information is retrieved using vector embeddings.
4. LLM generates context-aware response.
5. ML models provide prediction if required.

---

## 📊 Machine Learning Models

- Crop Recommendation (Classification)
- Disease Prediction Model
- Feature Engineering & Data Preprocessing

---

## 🔐 API Configuration

If using LLM API (Example: Together / OpenAI), add your API key in configuration file:

```python
llm = Together(
    model="meta-llama/Llama-2-70b-chat-hf",
    max_tokens=512,
    temperature=0.1,
    together_api_key="YOUR_API_KEY"
)
```

---

## 📂 Project Structure

```
AgriSaathi/
│── app.py
│── models/
│── dataset/
│── templates/
│── static/
│── requirements.txt
│── README.md
```

---

## 🎯 Future Improvements

- 📱 Mobile Application
- 🎙️ Voice-enabled chatbot
- 🌦️ Real-time Weather API Integration
- 🧠 Advanced Deep Learning Disease Detection

---

## 👨‍💻 Author

Siddhesh Ranjane  
B.Tech – Artificial Intelligence & Data Science  

---

⭐ If this project helped you, consider giving it a star!
