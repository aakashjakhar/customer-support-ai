import numpy as np
from backend.app.rag.embedding import embedding_model


def retrieve(query, index, chunks, top_k=3):
    """
    Retrieve the most relevant chunks for a query.
    """

    # Convert user query to embedding
    query_embedding = embedding_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search in FAISS
    distances, indices = index.search(query_embedding, top_k)

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks