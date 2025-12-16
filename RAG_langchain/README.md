# RAG System with Ollama, Chroma DB, and LangChain

This project sets up a Retrieval-Augmented Generation (RAG) system using local LLM via Ollama, Chroma DB for vector storage, and LangChain for orchestration.

## Prerequisites
- Python 3.8+
- VS Code
- Windows laptop with 8GB RAM, 1000GB HDD, 2GB GPU

## Step-by-Step Setup

### 1. Create and Activate Virtual Environment
- Open VS Code in the workspace `e:\Study\genAI\RAG_langchain`
- Open terminal in VS Code (PowerShell)
- Run: `python -m venv genAI`
- To activate (since execution policy may block, use the Python directly): Use `genAI\Scripts\python.exe` for commands

### 2. Install Dependencies
- Run: `genAI\Scripts\python.exe -m pip install -r requirements.txt`

### 3. Install Ollama
- Go to https://ollama.com/download
- Download the Windows installer
- Run the installer to install Ollama
- After installation, open a new terminal and run `ollama serve` (this starts the Ollama server in background)
- Pull a small model suitable for your machine: `ollama pull llama2:7b` (about 4GB, should fit in 8GB RAM)

### 4. Prepare Your PDF
- Place your private PDF file in the workspace directory, e.g., `sample.pdf`

### 5. Ingest PDF into Chroma DB
- Run: `genAI\Scripts\python.exe ingest.py`
- Enter the path to your PDF when prompted, e.g., `sample.pdf`
- This will load the PDF, split into chunks, create embeddings, and store in `./chroma_db`

### 6. Query the RAG System
- Ensure Ollama is running (`ollama serve` in another terminal)
- Run: `genAI\Scripts\python.exe query.py`
- Enter queries about the document
- Type 'quit' to exit

## Notes
- The embedding model `all-MiniLM-L6-v2` is small and efficient.
- If RAM is an issue, consider smaller Ollama models like `phi` or `tinyllama`.
- For better summarization, you can experiment with other models, but check memory usage.