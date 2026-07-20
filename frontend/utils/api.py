import requests

BASE_URL = "http://127.0.0.1:8000"


# ==========================
# Register
# ==========================
def register_user(username, email, password):

    data = {
        "username": username,
        "email": email,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/auth/register",
        json=data,
        timeout=10
    )


# ==========================
# Login
# ==========================
def login_user(email, password):

    data = {
        "email": email,
        "password": password
    }

    return requests.post(
        f"{BASE_URL}/auth/login",
        json=data,
        timeout=10
    )


# ==========================
# Chat
# ==========================
def send_message(user_id, message):

    data = {
        "user_id": user_id,
        "message": message
    }

    return requests.post(
        f"{BASE_URL}/chat",
        json=data,
        timeout=60
    )


# ==========================
# Chat History
# ==========================
def get_chat_history(user_id):

    return requests.get(
        f"{BASE_URL}/chat-history/{user_id}",
        timeout=10
    )