import os

import load_env as lenv
import google.generativeai as genai

from typing import List
from pymongo import MongoClient

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

client = MongoClient(lenv.mongodb_client)
db = client[lenv.mongodb_name]
collection = db[lenv.mongodb_collection]

geminiapi_key = lenv.geminiapi_key
model_embedding = lenv.model_embedding
genai.configure(api_key=geminiapi_key)

def main(clear: bool = True):
  if clear:
    clear_database()
  create_vectors()

def create_vectors():
  dirs = load_mds_dir()
  for dir in dirs:
    content = load_content(dir)
    chunks = chunkenizer(content)
    chunks = to_embedding(chunks, dir)
    add_chunks_in_database(chunks, collection)
  return True

def load_mds_dir() -> list[str]:
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

def embed(text):
  f = genai.embed_content(
    model=model_embedding,
    content=text,
    task_type="retrieval_document"
  )
  return f

def to_embedding(chunks: List[Document], doc: str):
  embed_chunk = []
  for chunk in chunks:
    embed_chunk.append({
      'document': doc, 
      'chunk': chunk.page_content, 
      'embedding': embed(chunk.page_content)
    })
  return embed_chunk

def add_chunks_in_database(chunks, collection):
  for chunk in chunks:
    collection.insert_one(chunk)

def clear_database():
  collection.drop()

if __name__ == "__main__":
  main()