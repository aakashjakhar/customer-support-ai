from backend.app.rag.document_loader import load_documents
from backend.app.rag.text_splitter import split_documents
from backend.app.rag.embedding import create_embeddings
from backend.app.rag.vector_store import create_vector_store
from backend.app.rag.retriever import retrieve


def test_rag():

    print("\nLoading Documents...")
    documents = load_documents()

    print("\nSplitting Documents...")
    chunks = split_documents(documents)

    print("\nCreating Embeddings...")
    embeddings = create_embeddings(chunks)

    print("\nCreating Vector Store...")
    index = create_vector_store(embeddings)

    # -----------------------------
    # Test Query
    # -----------------------------
    query = "I forgot my password"

    print("\nUser Query:")
    print(query)

    print("\nSearching Knowledge Base...\n")

    results = retrieve(query, index, chunks)

    print("=" * 70)

    for i, chunk in enumerate(results, start=1):

        print(f"\nResult {i}")
        print("-" * 70)
        print(chunk.page_content)
        print("\nSource:", chunk.metadata["source"])
        print("=" * 70)


if __name__ == "__main__":
    test_rag()