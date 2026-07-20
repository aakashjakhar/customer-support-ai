from backend.app.services.gemini_services import get_ai_response
from backend.app.services.rag_services import search_knowledge
from backend.app.memory.memory_manager import memory



def general_faq_agent(message: str):

    # Retrieve relevant information
    context = search_knowledge(message)
    
    history = memory.get_history()

    prompt = f"""
You are the General FAQ Assistant for TechMart Electronics.

Answer ONLY using the information from the Knowledge Base.

If the answer is not available in the Knowledge Base,
politely tell the customer that the information is unavailable.

Previous Conversation:
{history}

Knowledge Base:
{context}

Customer Question:
{message}
"""

    return get_ai_response(prompt)