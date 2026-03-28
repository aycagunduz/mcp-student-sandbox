import os
from dotenv import load_dotenv

load_dotenv()  # .env dosyasından değişkenleri yükle

AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
if not AWS_SECRET_KEY:
    raise ValueError("AWS_SECRET_KEY environment variable is not set")

def connect():
    print(f"Connecting with: {AWS_SECRET_KEY}")
