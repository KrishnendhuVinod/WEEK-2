import autogen
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")

print("AutoGen imported successfully!")
print("API Key loaded:", api_key is not None)
