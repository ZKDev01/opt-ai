"""
3. Mejorar la busqueda para que no solo recolepte un solo chunk, sino un valor k que se puede escoger
4. Mejorar los prompts a como dijo el profe
5. Mejorar el query
6. Lectura de CSV y mandar tabla a ia para que:
  1. Modelo de programacion no linea
  2. Solucion de un problema relacionado con la tabla en python
"""

import load_env as lenv
import pandas as pd

from pymongo import MongoClient

def main():
  df = load_collection()
  print(df.head())

def load_collection() -> pd.DataFrame:
  client = MongoClient(lenv.mongodb_client)
  db = client[lenv.mongodb_name]
  collection = db[lenv.mongodb_collection]
  documents = collection.find()
  df = pd.DataFrame(list(documents))
  return df

if __name__ == '__main__':
  main()
  