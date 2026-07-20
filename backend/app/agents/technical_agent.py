from backend.app.services.gemini_services import get_ai_response
from backend.app.services.rag_services import search_knowledge
from backend.app.memory.memory_manager import memory


def technical_agent(message: str):

    # Retrieve relevant knowledge
    context = search_knowledge(message)
    
    history = memory.get_history()

    prompt = f"""
You are a Technical Support Specialist.

Use ONLY the information provided below to answer the customer's question.

If the answer is not available in the knowledge base,
politely tell the customer that the information is unavailable.

Previous Conversation:
{history}

Knowledge Base:
{context}

Customer Question:
{message}
"""

    return get_ai_response(prompt)