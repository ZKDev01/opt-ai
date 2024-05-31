import os
import load_env as lenv
import pandas as pd

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage

from pymongo import MongoClient

client = MongoClient('localhost')
db = client['embedding_document_database']
collection = db['testing']

embedding = GoogleGenerativeAIEmbeddings(
  model='models/embedding-001',
  google_api_key=lenv.geminiapi_key)

def testing_embedding():
  result = embedding.embed_query('Hola Mundo')
  print(result[:5])

def test_convert_obj():
  t = [
    {
      'query': 'hola mundo',
      'embedding': [0.4, 0.3, 0.9]
    },
    {
      'query': 'xd',
      'embedding': [0.4, 0.9]
    }
  ]
  for i in t:
    # collection.insert_one(i)
    pass
  
  documents = collection.find()
  df = pd.DataFrame(list(documents))
  print(df)


if __name__ == '__main__':
  testing_embedding()
  pass
