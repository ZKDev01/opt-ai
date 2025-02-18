from tabnanny import verbose
from typing import List
from chromadb import Client, Collection
from sentence_transformers import CrossEncoder
from langchain_core.documents import Document


#! fallo con streamlit 
class Vectorstore : 
  model:CrossEncoder
  collection:Collection
  
  def __init__(self,
      collection_name:str,
      documents:List[Document]
    ) -> None:
    self.model:CrossEncoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512)
    client:Client = Client()
    self.collection:Collection = client.get_or_create_collection(collection_name)
    self.collection.add( ids=[ f"Doc {i+1}" for i,_ in enumerate(documents) ], documents=[ doc.page_content for doc in documents ] )
    
  def search_similar_documents(self,query_texts:List[str],n_results:int=3) -> List:
    results = self.collection.query(query_texts=query_texts, n_results=n_results)
    return results['documents'][0]
  
