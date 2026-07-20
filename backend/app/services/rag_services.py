from backend.app.rag.document_loader import load_documents
from backend.app.rag.text_splitter import split_documents
from backend.app.rag.embedding import create_embeddings
from backend.app.rag.vector_store import create_vector_store
from backend.app.rag.retriever import retrieve




# Load all documents
documents = load_documents()

# Split into chunks
chunks = split_documents(documents)

# Create embeddings
embeddings = create_embeddings(chunks)

# Create FAISS index
index = create_vector_store(embeddings)

print("Knowledge Base Ready!")


def search_knowledge(query: str, top_k: int = 3):
    """
    Search the knowledge base and return the most relevant chunks.
    """

    results = retrieve(query, index, chunks, top_k)

    context = ""

    for chunk in results:
        context += chunk.page_content + "\n\n"

    return context