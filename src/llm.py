import dotenv
import os

from create_vectorstore import FAISS_VECTORSTORE
from prompt_template import prompt_modify_query, prompt_ask_yes_or_not

from typing import List, Tuple
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

dotenv.load_dotenv()
os.environ.setdefault('google_api_key', os.getenv('google_api_key')) 

llm_model = 'models/gemini-1.5-pro'
llm_embedding = 'models/embedding-001'

model = GoogleGenerativeAI(
  model=llm_model
)
embedding = GoogleGenerativeAIEmbeddings(
  model=llm_embedding
)

class LLM_main():
  def __init__(self, k: int = 1) -> None:
    if (not isinstance(k, int)) or k < 1:
      raise("The k value does not int")
    
    self.vs = FAISS_VECTORSTORE()
    self.k_param = k
    

  def find_k_best_passage(self, query: str):
    result: List[Tuple[Document, float]] = self.vs.vs.similarity_search_with_relevance_scores(query=query, k=self.k_param)
    print(result)
  
  def make_prompt(self, relevant_passages: List[Document]):
    pass
  
  def transform_query(self, query):
    return query

  def answer_query(self, query):
    
    return ''

def testing_llm():
  llm = LLM_main(k=3)
  llm.transform_query("arboles")

if __name__ == '__main__':
  testing_llm()
  pass