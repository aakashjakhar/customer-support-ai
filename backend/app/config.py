import os
from dotenv import load_dotenv

load_dotenv("backend/.env")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")