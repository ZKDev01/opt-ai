import os

import load_env as lenv 

from pymongo import MongoClient

# from langchain_community.document_loaders import 
from langchain.text_splitter import MarkdownHeaderTextSplitter

def main():
  client = MongoClient(lenv.mongodb_client)
  db = client[lenv.mongodb_name]
  collection = db[lenv.mongodb_collection]
  run = create_vectors(collection)
  if run:
    print("BASE DE DATOS CREADA") 
  else:
    print("ERROR") 

def create_vectors(collection):
  dirs = load_mds_dir()
  for dir in dirs:
    content = load_content(dir)

  return 
  # TARGET
  dir = '' 
  chunks = load_doc(dir)
  # for every chunk
  chunk = dir
  embedding = to_embedding(chunks)
  obj = convert_obj(chunk, embedding)
  add_vector(obj, collection)

  pass

def load_mds_dir() -> list[str]:
  # TODO OK
  dirs =  os.listdir(lenv.data_path)
  dirs = [(lenv.data_path + "\\" + dir) for dir in dirs]
  return dirs

def load_content(dir: str):
  # TODO OK
  content = ''
  with open(dir, 'r', encoding='utf-8') as file:
    content = file.read()
  return content

def chunkenizer(content: str):
  headers_to_split_on = [
    ("#", "H1"),
    ("##", "H2"),
    ("###", "H3"),
    ("####", "H4"),
    ("#####", "H5")]
  
  md_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
  chunks = md_splitter.split_text(content)
  
  for chunk in chunks:
    print("----------------")
    print(chunk)
  
def to_embedding(chunks: str):
  # embedding chunks
  pass

def convert_obj(chunk: str, embedding: str):
  pass

def add_vector(obj, collection):
  collection.insert_one({
    'element1': 10,
    'element2': 11
  })

def clear_database():
  pass

if __name__ == "__main__":
  # main()
  dirs = load_mds_dir()
  content = load_content(dirs[0])
  chunkenizer(content)
  