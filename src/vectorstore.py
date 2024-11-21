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
# endregion


class FAISS_VECTORSTORE:

  def __init__(self, folder_path: str, load:bool=True, chunks:List[Document] = []) -> None:
    if load:
      self.vectorstore = FAISS.load_local(
        folder_path=folder_path,
        embeddings=embed,
        allow_dangerous_deserialization=True
      )
    else:
      self.vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embed
      )
      self.vectorstore.save_local(folder_path=folder_path)

  def similarity_search ( self, query:str, k:int=3 ) -> List[Document]:
    result:List[Document] = self.vectorstore.similarity_search(query=query, k=k)
    return result



