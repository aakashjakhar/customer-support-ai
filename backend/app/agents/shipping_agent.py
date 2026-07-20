from backend.app.services.rag_services import search_knowledge
from backend.app.services.gemini_services import get_ai_response
from backend.app.memory.memory_manager import memory


def shipping_agent(query: str):

    context = search_knowledge(query)
    
    history = memory.get_history()

    prompt = f"""
You are the Shipping Support Agent 

Use ONLY the information provided in the knowledge base.

Do not make up any information.

If the answer is not available in the knowledge base,
politely inform the customer.

Previous Conversation:
{history}

Knowledge Base:
{context}

Customer Question:
{query}

Provide a clear and professional answer.
"""

    return get_ai_response(prompt)