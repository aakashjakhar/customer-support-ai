import faiss
import numpy as np


def create_vector_store(embeddings):
    """
    Create a FAISS index from embeddings.
    """

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(embeddings).astype("float32")

    index.add(vectors)

    return index