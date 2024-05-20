import os
import dotenv

telegram_token = ''
telegram_username = ''
geminiapi_key = ''
model_embedding = 'models/embedding-001'

if __name__ != "__main__":
  dotenv.load_dotenv()
  telegram_token = os.getenv("telegram_token") 
  telegram_username = os.getenv("telegram_username")
  geminiapi_key = os.getenv("geminiapi_key")