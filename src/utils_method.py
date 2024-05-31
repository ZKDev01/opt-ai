import load_env as lenv
import pandas as pd

from pymongo import MongoClient

def load_collection() -> pd.DataFrame:
  client = MongoClient(lenv.mongodb_client)
  db = client[lenv.mongodb_name]
  collection = db[lenv.mongodb_collection]
  documents = collection.find()
  df = pd.DataFrame(list(documents))
  return df