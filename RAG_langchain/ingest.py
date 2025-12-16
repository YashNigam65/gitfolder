import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def ingest_pdf(pdf_path, persist_directory='./chroma_db'):
    # Load PDF
    loader = PyPDFLoader(pdf_path) # Create a PDF loader instance
    documents = loader.load()  # List of Document objects

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  # Split into chunks
    docs = text_splitter.split_documents(documents) #  List of chunked Document objects

    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2') # Create embeddings instance

    # Vector store
    vectorstore = Chroma.from_documents(docs, embeddings, persist_directory=persist_directory)

    print("Embeddings stored in Chroma DB.")

if __name__ == "__main__":
    pdf_path = "E:\Study\genAI\RAG_langchain\yash_kumar_cv.pdf"  # Update with your PDF path
    ingest_pdf(pdf_path)