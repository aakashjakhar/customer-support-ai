from rapidfuzz import fuzz

from backend.app.rag.document_loader import load_documents
from backend.app.rag.text_splitter import split_documents


# Load and split knowledge-base documents once
documents = load_documents()
chunks = split_documents(documents)

print(f"Knowledge Base Ready! Loaded {len(chunks)} chunks.")


def search_knowledge(query: str, top_k: int = 3) -> str:
    """
    Search the knowledge base using lightweight fuzzy matching.

    This avoids Sentence Transformers, PyTorch and FAISS,
    which exceed Render's free 512 MB memory limit.
    """

    if not query or not query.strip():
        return ""

    query = query.strip().lower()
    scored_chunks = []

    for chunk in chunks:
        content = chunk.page_content.strip()

        if not content:
            continue

        score = fuzz.token_set_ratio(
            query,
            content.lower()
        )

        scored_chunks.append((score, content))

    scored_chunks.sort(
        key=lambda item: item[0],
        reverse=True
    )

    best_chunks = scored_chunks[:top_k]

    relevant_chunks = [
        content
        for score, content in best_chunks
        if score >= 20
    ]

    return "\n\n".join(relevant_chunks)