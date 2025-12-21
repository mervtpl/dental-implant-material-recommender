import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

try:
    # 'models/' takısını kaldırarak direkt ismi yaz
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Diş implantı projem için test mesajı."
    )
    print("Başarılı! Yanıt:", response.text)
except Exception as e:
    print(f"Hata detayı: {e}")