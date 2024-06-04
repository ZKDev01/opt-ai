from typing import List
import dotenv
import os

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document

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

current = os.getcwd()
doc_dir = '\\database\\doc'

DATA_PATH = current + doc_dir
dir = os.listdir(DATA_PATH)

def search_docs():
  docs_dir = os.listdir(DATA_PATH)
  docs_dir = [DATA_PATH + '\\' + item for item in docs_dir]
  return docs_dir

def load_contents(docs_dir: list[str]):
  def load_content(doc_dir: str):
    content = ''
    with open(doc_dir, 'r', encoding='utf-8') as file:
      content = file.read()
    return content  
  docs_content = [load_content(doc_dir=doc_dir) for doc_dir in docs_dir]
  return docs_content 

def chunkenizer(content: str):
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1024,
    chunk_overlap = 204,
    length_function = len
  )
  chunks = text_splitter.create_documents([content])
  return chunks

def create_chunks():
  docs_dir = search_docs()
  docs_content = load_contents(docs_dir)
  chunks: List[Document] = []
  for doc_content in docs_content:
    for item in chunkenizer(doc_content):
      chunks.append(item)
  return chunks

class FAISS_VECTORSTORE():
  def __init__(self) -> None:
    chunks = create_chunks()
    self.vs = FAISS.from_documents(
      documents=chunks, 
      embedding=embedding)
  def add_document_to_vectorstore():
    pass
  def del_document_from_vectorstore():
    pass
  def del_documents_from_vectorstore():
    pass

class MONGODB_VECTORSTORE():
  pass

def testing_faiss():
  vectorstore = FAISS_VECTORSTORE()
  query = "Que son los arboles?"
  results = vectorstore.vs.similarity_search(query, k=1)
  for result in results:
    print(f"RESULTADO: {result}")

if __name__ == "__main__":
  pass
