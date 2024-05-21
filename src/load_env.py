import os
import dotenv

telegram_token = ''
telegram_username = ''
geminiapi_key = ''

model_llm = 'models/gemini-pro'
model_embedding = 'models/embedding-001'

if __name__ == "__main__":
  print(f"""
  Model LLM: {model_llm}
  Model Embedding: {model_embedding}
  """)
else:
  dotenv.load_dotenv()
  telegram_token = os.getenv("telegram_token") 
  telegram_username = os.getenv("telegram_username")
  geminiapi_key = os.getenv("geminiapi_key")