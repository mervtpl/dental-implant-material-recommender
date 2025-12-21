import os
from google import genai
from dotenv import load_dotenv



load_dotenv()

client= genai.Client()

model ="gemini-2.5-flash"

def ask_gemini(prompt: str) -> str:
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text
