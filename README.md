# 🧠 Medical Chatbot using RAG and LLM

A smart and interactive medical assistant that answers health-related queries based on medical research documents using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs).

## 🔍 What it does

This chatbot allows users to ask questions about various diseases and conditions (e.g., symptoms, treatments, medicines, and precautions). It retrieves relevant content from uploaded medical documents and generates accurate, context-aware answers using a pre-trained language model.

---

## 🧪 Features

- ✅ **Retrieval-Augmented Generation (RAG)** pipeline
- 🤖 **LLM-based question answering** using `google/flan-t5-small` or other HuggingFace models
- 📄 **Contextual document retrieval** using FAISS vector store
- 📚 Loads `.txt` research files from a `docs/` folder
- 🧠 Supports disease queries like asthma, anemia, cancer, fever, diabetes, flu, vomiting, etc.
- 🌐 **Streamlit frontend** for real-time interaction
- 🔐 Environment variable support for secure API keys (`.env`)

---

