from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

def query_rag(persist_directory='./chroma_db', model_name='phi'):
    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # Load vector store
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)

    # Retriever
    retriever = vectorstore.as_retriever()

    # LLM
    llm = ChatOllama(model=model_name)

    while True:
        query = input("Enter your query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        # Get relevant documents
        docs = retriever.invoke(query) # List of Document objects
        context = "\n".join([doc.page_content for doc in docs])
        prompt = f"Context from document:\n{context}\n\nQuestion: {query}\nAnswer:"
        result = llm.invoke(prompt)
        print("Answer:", result.content)

if __name__ == "__main__":
    query_rag()