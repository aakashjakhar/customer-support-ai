import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ClientError

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env")

# Create Gemini Client
client = genai.Client(api_key=api_key)


def get_ai_response(prompt: str) -> str:
    """
    Send prompt to Gemini and return the generated response.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except ClientError as e:
        error_message = str(e)

        if "RESOURCE_EXHAUSTED" in error_message or "429" in error_message:
            return (
                "The AI service is temporarily unavailable because the Gemini API quota "
                "has been exceeded. Please try again later."
            )

        return f"Gemini API Error: {error_message}"

    except Exception as e:
        return f"Unexpected error: {str(e)}"
