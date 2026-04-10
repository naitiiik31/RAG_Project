# 📚 RAG Book Assistant

A Retrieval-Augmented Generation (RAG) system that lets you upload any PDF and ask questions about it. Built with LangChain, ChromaDB, MistralAI, and Streamlit.

---

## Demo

Upload a PDF → Click "Create Vector Database" → Ask questions → Get grounded answers.

---

## How It Works

```
PDF Upload → Text Chunking → Embeddings (MistralAI) → ChromaDB Vector Store
                                                              ↓
                                          User Query → MMR Retrieval → MistralAI LLM → Answer
```

1. **Document Loading** – PDF is loaded and parsed using `PyPDFLoader`
2. **Chunking** – Text is split into 1000-character chunks with 200-character overlap using `RecursiveCharacterTextSplitter`
3. **Embeddings** – Each chunk is embedded using MistralAI Embeddings
4. **Vector Store** – Embeddings stored in ChromaDB for fast similarity search
5. **Retrieval** – MMR (Maximal Marginal Relevance) retrieval fetches the top-4 relevant, diverse chunks
6. **Generation** – MistralAI LLM answers strictly based on retrieved context — no hallucinations

---

## Features

- Upload any PDF and query it in natural language
- MMR-based retrieval for diverse, relevant context
- Strict prompt design: model only answers from document context
- Graceful fallback: responds with *"I could not find the answer in the document"* when the answer isn't present
- Clean Streamlit UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | MistralAI (`mistral-small-2506`) |
| Embeddings | MistralAI Embeddings |
| Vector Store | ChromaDB |
| Framework | LangChain |
| PDF Parsing | PyPDFLoader |

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/naitiiik31/RAG_Project.git
cd RAG_Project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the root directory:

```
MISTRAL_API_KEY=your_mistral_api_key_here
```

Get your API key at [console.mistral.ai](https://console.mistral.ai)

### 4. Run the app

```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your browser (default: `http://localhost:8501`)
2. Upload a PDF using the file uploader
3. Click **"Create Vector Database"** and wait for processing
4. Type your question in the text input
5. Get an answer grounded in your document

---

## Project Structure

```
RAG_Project/
├── app.py               # Main Streamlit app (upload + query UI)
├── createDB.py          # Standalone script to pre-build vector DB from a PDF
├── main.py              # CLI-based query interface
├── requirements.txt     # Dependencies
├── .env                 # API keys (not committed)
├── document loaders/    # Sample PDF documents
├── vector store/        # Vector store experiments
└── retriers/            # Retrieval strategy experiments
```

---

## Requirements

```
langchain
langchain-community
langchain-mistralai
langchain-text-splitters
chromadb
streamlit
pypdf
python-dotenv
```

---

## Future Improvements

- Support for multiple PDFs simultaneously
- Chat history / multi-turn conversation
- Source highlighting (show which page the answer came from)
- Reranking layer for improved retrieval accuracy
- Deploy on Streamlit Cloud or HuggingFace Spaces
