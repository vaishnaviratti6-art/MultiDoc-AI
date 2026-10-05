# 📚 MultiDoc AI

## Multi-Document Retrieval-Augmented Question Answering System

MultiDoc AI is an intelligent document question-answering system that allows users to upload multiple PDF, DOCX, and TXT documents and ask questions about their content.

The system uses Retrieval-Augmented Generation (RAG) to retrieve relevant document content and generate answers using Llama 3.2 through Ollama.

## ✨ Features

- 📄 Upload PDF, DOCX and TXT documents
- 🔍 Extract text from documents
- ✂️ Split documents into smaller chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🗄️ Store embeddings using ChromaDB
- 🔎 Retrieve relevant document content
- 🤖 Generate answers using Llama 3.2 and Ollama
- 📚 Display source documents
- 📑 Support multiple documents
- 💬 Chat history
- 🌐 Streamlit-based user interface

## 🛠️ Technology Stack

- Python
- Streamlit
- Ollama
- Llama 3.2
- ChromaDB
- Sentence Transformers
- PyPDF
- Python-docx
- NumPy

## 🔄 System Workflow

Document Upload  
↓  
Text Extraction  
↓  
Text Chunking  
↓  
Embedding Generation  
↓  
ChromaDB Storage  
↓  
Question Embedding  
↓  
Relevant Chunk Retrieval  
↓  
Llama 3.2  
↓  
Answer + Sources

## 📂 Project Structure

```text
MultiDoc/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── config/
├── ingestion/
├── embeddings/
├── vectorstore/
├── retrieval/
├── llm/
├── rag/
├── ui/
├── utils/
│
└── data/
    ├── uploads/
    └── chroma/