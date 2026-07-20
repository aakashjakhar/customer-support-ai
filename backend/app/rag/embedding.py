from sentence_transformers import SentenceTransformer

# Load the embedding model only once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Convert text chunks into vector embeddings.
    """

    texts = [chunk.page_content for chunk in chunks]

    embeddings = embedding_model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings