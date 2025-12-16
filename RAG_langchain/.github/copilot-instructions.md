# Copilot Instructions for RAG LangChain Project

## Project Overview
This is a Retrieval-Augmented Generation (RAG) system built with LangChain, using Ollama for local LLM inference, Chroma DB for vector storage, and Sentence Transformers for embeddings. It allows querying private PDF documents for accurate, context-aware answers.

## Architecture
- **Data Flow**: PDF → Text Splitting → Embeddings → Chroma Vector Store → Retrieval → LLM Generation
- **Key Components**:
  - `ingest.py`: Loads PDF, splits text, creates embeddings, stores in Chroma
  - `query.py`: Loads vector store, sets up RAG chain with Ollama LLM, handles user queries
- **Why this structure**: Separates ingestion from querying for reusability; uses local components to avoid API costs and ensure privacy

## Developer Workflows
- **Setup**: Create venv `genAI`, activate via `genAI\Scripts\python.exe`, install deps from README
- **Ingest Document**: Run `genAI\Scripts\python.exe ingest.py`, provide PDF path
- **Query**: Run `genAI\Scripts\python.exe query.py`, ensure `ollama serve` is running
- **Debugging**: Check Chroma DB in `./chroma_db`; verify Ollama model with `ollama list`

## Conventions and Patterns
- **Embeddings**: Use `SentenceTransformerEmbeddings` with `'all-MiniLM-L6-v2'` for efficiency on low-RAM machines
- **Text Splitting**: `RecursiveCharacterTextSplitter` with chunk_size=1000, overlap=200
- **LLM**: Ollama with models like `'llama2:7b'`; chain type "stuff" for simple retrieval
- **Vector Store**: Chroma with persist_directory for local storage
- **Error Handling**: Basic input prompts; no advanced error handling yet

## Integration Points
- **Ollama**: Local LLM server; start with `ollama serve`, pull models via `ollama pull`
- **Chroma DB**: Local vector DB; persists to disk for reuse
- **LangChain**: Orchestrates retrieval and generation; uses `RetrievalQA` for RAG

## Key Files
- [ingest.py](ingest.py): Document ingestion pipeline
- [query.py](query.py): RAG query interface
- [README.md](README.md): Setup and usage instructions