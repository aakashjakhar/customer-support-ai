from backend.app.utils.text_utils import fuzzy_match


def match_intent(message: str, keywords: list):

    words = message.lower().split()

    for word in words:

        if fuzzy_match(word, keywords):
            return True

    return False


def detect_intent(message: str):

    message = message.lower()

    technical_keywords = [
    "login",
    "not turning on",
    "turning on",
    "turning off",
    "not charging",
    "not displaying",
    "hardware problem",
    "log in",
    "sign in",
    "password",
    "otp",
    "account",
    "technical",
    "issue",
    "error",
    "bug",
    "crash",
    "freeze",
    "hang",
    "not working",
    "unable",
    "failed",
    "exception",
    "installation",
    "install",
    "network",
    "wifi",
    "internet",
    "software",
    "hardware",
    "screen",
    "display",
    "driver",
    "configuration",
    "api",
    "server",
    "laptope",
    "phone",
    "database"
]

    billing_keywords = [
    "payment",
    "paid",
    "bill",
    "billing",
    "invoice",
    "receipt",
    "gst",
    "tax",
    "price",
    "pricing",
    "cost",
    "subscription",
    "renew",
    "renewal",
    "refund",
    "money",
    "charge",
    "charged",
    "transaction",
    "upi",
    "credit card",
    "debit card",
    "emi",
    "discount",
    "coupon"
]

    shipping_keywords = [
    "order",
    "delivery",
    "shipping",
    "track",
    "tracking",
    "dispatch",
    "courier",
    "shipment",
    "address",
    "expected delivery",
    "delay",
    "delayed",
    "where is my order",
    "package",
    "arrived",
    "received"
]

    faq_keywords = [
    "business hours",
    "working hours",
    "opening hours",
    "contact",
    "support",
    "customer care",
    "company",
    "about",
    "location",
    "email",
    "phone number",
    "return policy",
    "privacy policy",
    "terms"
]
    
    Warranty_keywords = [
    "warranty",
    "under warranty",
    "guarantee",
    "replacement",
    "replace",
    "repair",
    "repairing",
    "repair center",
    "service center",
    "manufacturing defect",
    "factory defect",
    "hardware failure",
    "claim",
    "claim warranty",
    "warranty period",
    "broken",
    "damaged"
]
    
    assistant_keywords = [

    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening",
    "good afternoon",

    "who are you",
    "tell me about yourself",
    "about yourself",
    "introduce yourself",

    "what can you do",
    "how can you help",
    "help me",
    "your capability",
    "your features",

    "thank you",
    "thanks",
    "bye",
    "goodbye"
]
    
    
    
    if match_intent(message, technical_keywords):
       return "Technical Support"

    if match_intent(message, billing_keywords):
       return "Billing"

    if match_intent(message, shipping_keywords):
       return "Shipping"

    if match_intent(message, faq_keywords):
       return "General FAQ"
    
    if match_intent(message, Warranty_keywords):
       return "Warranty"    
   
    if match_intent(message,assistant_keywords):
        return "Assistant"

    return "AI ASSISTANCE CHATBOAT"