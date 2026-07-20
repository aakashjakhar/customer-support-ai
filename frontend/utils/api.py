import requests

BASE_URL = "https://customer-support-ai-1-5yu6.onrender.com"


def parse_response(response):
    try:
        return response.status_code, response.json()
    except ValueError:
        return response.status_code, {
            "detail": response.text or "Invalid response from backend"
        }


def register_user(username, email, password):
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={
                "username": username,
                "email": email,
                "password": password
            },
            timeout=60
        )

        return parse_response(response)

    except requests.exceptions.RequestException as error:
        return 500, {
            "detail": f"Could not connect to backend: {error}"
        }


def login_user(email, password):
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password
            },
            timeout=60
        )

        return parse_response(response)

    except requests.exceptions.RequestException as error:
        return 500, {
            "detail": f"Could not connect to backend: {error}"
        }


def send_message(user_id, message):
    try:
        response = requests.post(
            f"{BASE_URL}/chat",
            json={
                "user_id": int(user_id),
                "message": message
            },
            timeout=120
        )

        return parse_response(response)

    except requests.exceptions.RequestException as error:
        return 500, {
            "detail": f"Could not connect to backend: {error}"
        }

    except (TypeError, ValueError):
        return 400, {
            "detail": "Invalid user ID."
        }


def get_chat_history(user_id):
    try:
        response = requests.get(
            f"{BASE_URL}/chat/history/{int(user_id)}",
            timeout=60
        )

        return parse_response(response)

    except requests.exceptions.RequestException as error:
        return 500, {
            "detail": f"Could not connect to backend: {error}"
        }

    except (TypeError, ValueError):
        return 400, {
            "detail": "Invalid user ID."
        }