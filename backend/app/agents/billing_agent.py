from backend.app.services.rag_services import search_knowledge
from backend.app.services.gemini_services import get_ai_response
from backend.app.memory.memory_manager import memory


def billing_agent(query: str):

    context = search_knowledge(query)
    
    history = memory.get_history()

    prompt = f"""
You are the Billing Support Agent for TechMart Electronics.

Use ONLY the information provided in the knowledge base.

If the answer is not available in the knowledge base,
politely say that the information is unavailable.


Previous Conversation:
{history}

Knowledge Base:
{context}

Customer Question:
{query}

Provide a clear and professional answer.
"""

    return get_ai_response(prompt)