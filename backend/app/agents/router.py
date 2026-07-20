from backend.app.agents.fallback_agent import fallback_agent
from backend.app.agents.billing_agent import billing_agent
from backend.app.agents.technical_agent import technical_agent
from backend.app.agents.general_faq_agent import general_faq_agent
from backend.app.agents.shipping_agent import shipping_agent
from backend.app.agents.warranty_agent import warranty_agent
from backend.app.agents.assistant_agent import assistant_agent


def route_intent(intent: str, message: str):

    if intent == "Billing":
        return billing_agent(message)

    elif intent == "Technical Support":
        return technical_agent(message)
    
    elif intent == "General FAQ":
      return general_faq_agent(message)
  
  
    elif intent == "Shipping":
        return shipping_agent(message) 
    
    elif intent == "Warranty":
        return warranty_agent(message)
    
    elif intent == "Assistant":
         return assistant_agent(message)

    return fallback_agent(message)