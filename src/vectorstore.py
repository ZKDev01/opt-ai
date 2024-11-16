import os 
import markdown
from typing import (
  List,
  Dict
)

from src.core import (
  get_model,
  get_embedding
)

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS



# region: GLOBAL VAR
model = get_model()
embed = get_embedding()

current = os.getcwd()
faiss_dir = '\\faiss\\'

FAISS_PATH = current + faiss_dir
# endregion







#! extract the format dir.split('.')[-1]





















def chunkenizer(content: str) -> List[Document]:
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1024,
    chunk_overlap = 204,
    length_function = len
  )
  chunks = text_splitter.create_documents([content])
  return chunks


""" 


def create_chunks() -> List[Document]:
  docs_dir = search_docs()
  docs_content = load_contents(docs_dir)
  chunks: List[Document] = []
  for doc_content in docs_content:
    document = Document(page_content=doc_content)
    chunks.append(document)  
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



  def similarity_search(self, query: str, k: int = 3) -> list[str]:
    if not k > 0:
      raise Exception("k no puede ser negativo ni 0")
    results = self.__vs.similarity_search(query=query, k=k)
    results_content = [result.page_content for result in results]
    return results_content

"""
