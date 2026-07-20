from backend.app.services.rag_services import search_knowledge
from backend.app.services.gemini_services import get_ai_response
from backend.app.memory.memory_manager import memory


def warranty_agent(query: str):

    context = search_knowledge(query)
    
    history = memory.get_history()
    

    prompt = f"""
You are the Warranty Support Agent for TechMart Electronics.

Answer ONLY using the information from the knowledge base.

Do not invent information.

If the answer is not present,
politely tell the customer that it is unavailable.


Previous Conversation:
{history}

Knowledge Base:
{context}

Customer Question:
{query}

Provide a professional answer.
"""

    return get_ai_response(prompt)