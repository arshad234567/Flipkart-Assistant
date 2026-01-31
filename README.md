# 🛒 Flipkart AI Assistant

An **AI-powered shopping assistant** inspired by Flipkart that understands natural language queries and intelligently routes them to the correct backend logic (FAQ or product search) using **Semantic Routing**, **LLMs**, and **Vector Databases**.

This project demonstrates a **real-world AI backend architecture** used in modern e-commerce assistants.

---

## 🚀 Features

- 🔀 **Semantic Intent Routing**
  - Automatically classifies user queries into:
    - FAQ-related queries
    - Product search (SQL-based) queries
- 🧠 **LLM-powered SQL Generation**
  - Converts natural language product queries into SQL
- 🗄️ **SQLite Product Database**
  - Stores product details such as brand, price, discount, and ratings
- 📦 **ChromaDB Vector Store**
  - Semantic search for FAQ-style questions
- 🖥️ **Streamlit UI**
  - Interactive and user-friendly interface
- 🔐 **Secure Environment Handling**
  - API keys managed via `.env` (never committed)

---

## 🧱 System Architecture

User Query
↓
Semantic Router (sentence-transformers)
↓
┌───────────────┬──────────────────┐
│ │ │
FAQ Route SQL Route Fallback
│ │
ChromaDB LLM → SQL → SQLite
│ │
Answer Product Results




---

## 🛠️ Tech Stack

- **Python 3.11**
- **semantic-router (v0.0.17)**
- **sentence-transformers**
- **ChromaDB**
- **SQLite**
- **Pandas**
- **Streamlit**
- **Groq LLM API**
- **Pydantic v2**

---

## 📂 Project Structure

Flipkart Assistant/
│
├── app/
│ ├── main.py # Streamlit entry point
│ ├── router.py # Semantic routing logic
│ ├── sql.py # SQL execution logic
│ ├── faq.py # FAQ ingestion & retrieval (ChromaDB)
│ ├── db.sqlite # Product database (ignored in git)
│ └── resources/ # FAQ data files
│
├── .gitignore
└── README.md



