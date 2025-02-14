import re
import numpy as np 

from typing import List, Dict
from chromadb import Client, Collection
from sentence_transformers import CrossEncoder
from langchain_core.documents import Document



class Vectorstore : 
  def __init__(self, documents:List[Document], vectorstore:bool=False):
    self.model:CrossEncoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2', max_length=512)
    
    if not vectorstore:
      client:Client = Client()
      self.collection:Collection = client.get_or_create_collection("collection")
      self.collection.add( ids=[ f"Doc {i+1}" for i,_ in enumerate(documents) ], documents=[ doc.page_content for doc in documents ] )
    
    else:
      ... 

  def query(self,query_texts:List[str], n_results:int=3) -> None:
    results = self.collection.query(query_texts=query_texts, n_results=n_results)
    scores:Dict = { }
    return results
    for query in query_texts:
      scores[query] = self.model.predict( [(query,doc) for doc in results['documents'] ]  )
      #scores[query] = results['documents'][0][np.argmax(scores[query])]
    return scores

