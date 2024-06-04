import textwrap

import load_env as lenv
import pandas as pd
import numpy as np
import google.generativeai as genai

from typing import List 

genai.configure(api_key=lenv.geminiapi_key)

def find_best_passage(query: str, df: pd.DataFrame, k=1):
  query_embedding = genai.embed_content(
    model=lenv.model_embedding,
    content=query,
    task_type="retrieval_query"
  )

  print("QUERY EMBEDDING")
  print(query_embedding['embedding'])
  
  print("DATAFRAME EMBEDDING")
  print(np.stack(df['embedding']))

  dot_products = np.dot(np.stack(df['embedding']), query_embedding["embedding"])
  idx = np.argmax(dot_products)
  return df.iloc[idx]['chunk']

def clean_passages(passage: str):
  passage = passage.replace("'", "").replace('"', "").replace("\n", " ").lower()
  return passage

def make_unique_passage(passages: List[str]):
  unique = ''
  for i in range(len(passages)):
    line = f'Document {i+1}: {passages[i]} \n'
    unique=unique+line
  return unique

def make_prompt(query, relevant_passages: List[str]):
  relevant_passages = [clean_passages(relevant_passage) for relevant_passage in relevant_passages]
  prompt = f"""
  Eres un bot útil e informativo que responde preguntas utilizando texto del pasaje de referencia incluido a continuación \
  
  Asegúrate de responder incluyendo toda la información relevante. \
  
  Asegúrate de desglosar conceptos complicaados y mantener un tono amigable y conversacional \
  
  Si el pasaje no es relevante para la respuesta no respondas la pregunta \
  

  QUESTION: '{query}'
  
  PASSAGES:
  {make_unique_passage(relevant_passages)}
  ANSWER:
  """
  return prompt

def __testing_module1():
  query = 'Hola Mundo'
  passages = ['Hola Mundo', 'XD']
  make_prompt(query, passages)

if __name__ == "__main__":
  # __testing_module1()
  pass