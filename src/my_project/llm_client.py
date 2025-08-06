"""LLM client for generating responses."""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


def setup_client():
    """Setup the Gemini client."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not set in .env file")
    return genai.Client(api_key=api_key)


def generate_response(prompt, model="models/gemini-2.5-flash-lite"):
    """Generate response for a given prompt."""

    client = setup_client()
    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    return response.text
