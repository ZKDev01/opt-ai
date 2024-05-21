import src.load_env as lenv 

import os
import google.generativeai as genai 
import pandas as pd 

geminiapi_key = lenv.geminiapi_key
model_embedding = lenv.model_embedding
genai.configure(api_key=geminiapi_key)
model_embedding = 'models/embedding-001'

original = os.getcwd() + "\\database\\doc"
dirs = os.listdir(original)

def embed(title, text):
  return genai.embed_content(
    model=model_embedding,
    content=text,
    task_type="retrieval_document",
    title=title)["embedding"]

def main():
  database = []
  for dir in dirs:
    with open(original + '\\' + dir, encoding='utf-8') as file:
      result = file.read()
    database.append((dir, result))

  df = pd.DataFrame(database)
  df.columns = ['Title', 'Text']
  df['Embeddings'] = df.apply(lambda row: embed(row['Title'], row['Text']), axis=1)

  # TODO mejorar a Chroma 
  df.to_json(os.getcwd() + "\\database\\database.json")

if __name__ == "__main__":
  main()