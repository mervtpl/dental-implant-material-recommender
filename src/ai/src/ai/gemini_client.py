import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    return model

def ask_gemini(prompt):
    model = get_gemini_client()
    response = model.generate_content(prompt)
    return response.text