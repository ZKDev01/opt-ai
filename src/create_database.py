import os

import load_env as lenv

from typing import List
from pymongo import MongoClient

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def main(clear: bool = True):
  client = MongoClient(lenv.mongodb_client)
  db = client[lenv.mongodb_name]
  collection = db[lenv.mongodb_collection]
  if clear:
    clear_database(collection)
  run = create_vectors(collection)
  if run:
    print("BASE DE DATOS CREADA") 
  else:
    print("ERROR") 

def create_vectors(collection):
  dirs = load_mds_dir()
  for dir in dirs:
    content = load_content(dir)
    chunks = chunkenizer(content)
    chunks = to_embedding(chunks, dir)
    add_chunks_in_database(chunks, collection)
  return True


def load_mds_dir() -> list[str]:
  # TODO OK
  dirs =  os.listdir(lenv.data_path)
  dirs = [(lenv.data_path + "\\" + dir) for dir in dirs]
  return dirs

def load_content(dir: str):
  content = ''
  with open(dir, 'r', encoding='utf-8') as file:
    content = file.read()
  return content

def chunkenizer(content: str):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1024,
    chunk_overlap = 204,
    length_function = len,
    is_separator_regex=False
  )
  chunks = text_splitter.create_documents([content])
  return chunks
  
def embed():
  f = GoogleGenerativeAIEmbeddings(
    google_api_key=lenv.geminiapi_key,
    model=lenv.model_embedding
  )
  return f

def to_embedding(chunks: List[Document], doc: str):
  embedding = embed()
  embed_chunk = []
  for chunk in chunks:
    embed_chunk.append({
      'document': doc, 
      'chunk': chunk.page_content, 
      'embedding': embedding.embed_query(chunk.page_content)
    })
  return embed_chunk

def add_chunks_in_database(chunks, collection):
  for chunk in chunks:
    collection.insert_one(chunk)

def clear_database(collection):
  result = collection.drop()
  if result:
    print("La coleccion ha sido eliminada")
  else:
    print("No se pudo eliminar la coleccion")

if __name__ == "__main__":
  main()