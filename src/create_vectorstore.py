from typing import List
from tools import get_model, get_embedding
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document

model = get_model()
embedding = get_embedding()

current = os.getcwd()
doc_dir = '\\database\\docs-md'
faiss_dir = '\\database\\faiss'

DATA_PATH = current + doc_dir
FAISS_PATH = current + faiss_dir

dir = os.listdir(DATA_PATH)

def search_docs() -> list[str]:
  docs_dir = os.listdir(DATA_PATH)
  docs_dir = [DATA_PATH + '\\' + item for item in docs_dir]
  return docs_dir

def load_contents(docs_dir: list[str]) -> list[str]:
  def load_content(doc_dir: str):
    content = ''
    with open(doc_dir, 'r', encoding='utf-8') as file:
      content = file.read()
    return content  
  docs_content = [load_content(doc_dir=doc_dir) for doc_dir in docs_dir]
  return docs_content 

def chunkenizer(content: str) -> List[Document]:
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1024,
    chunk_overlap = 204,
    length_function = len
  )
  chunks = text_splitter.create_documents([content])
  return chunks

def create_chunks() -> List[Document]:
  docs_dir = search_docs()
  docs_content = load_contents(docs_dir)
  chunks: List[Document] = []
  for doc_content in docs_content:
    for item in chunkenizer(doc_content):
      chunks.append(item)
  return chunks

class FAISS_VECTORSTORE():

  def __init__(self, load: bool = False) -> None:
    if load: 
      self.__vs = FAISS.load_local(
        folder_path=FAISS_PATH, 
        embeddings=embedding,
        allow_dangerous_deserialization=True)
    else:
      chunks = create_chunks()
      self.__vs = FAISS.from_documents(
        documents=chunks[0:100], 
        embedding=embedding)
      
      i = 101
      while True:
        if i >= len(chunks):
          break
        if i + 99 >= len(chunks):
          extension = FAISS.from_documents(
            documents=chunks[i:len(chunks)],
            embedding=embedding
          )
          self.__vs.merge_from(extension)
          break
        extension = FAISS.from_documents(
          documents=chunks[i:i+99],
          embedding=embedding
        )
        i=i+100
      self.__vs.save_local(FAISS_PATH)

  def similarity_search(self, query: str, k: int = 3):
    if not k > 0:
      raise Exception("k no puede ser negativo ni 0")
    results = self.__vs.similarity_search(query=query, k=k)
    results_content = [result.page_content for result in results]
    return results_content

class MONGODB_VECTORSTORE():
  pass

# METODOS DE PRUEBA

def testing_create_vectorstore():
  FAISS_VECTORSTORE()

def testing_load_and_query_something():
  vs = FAISS_VECTORSTORE(load=True)
  result = vs.similarity_search(query='que es la apologetica', k=10)
  for item in result:
    print(item)

if __name__ == "__main__":
  testing_load_and_query_something()

