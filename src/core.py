import os 
import dotenv

from typing import List

from langchain_google_genai import (
  GoogleGenerativeAI, 
  GoogleGenerativeAIEmbeddings
)
from langchain_core.output_parsers import (
  StrOutputParser,
  CommaSeparatedListOutputParser,
  JsonOutputParser
)
from langchain_core.prompts import (
  ChatPromptTemplate
)
from langchain_core.pydantic_v1 import (
  BaseModel, 
  Field
)





# region: GLOBAL VAR
current = os.getcwd()
doc_dir = '\\database\\private'

DATA_PATH = current + doc_dir
# endregion



def load_env ( ) :
  dotenv.load_dotenv ( )
  os.environ.setdefault('google_api_key', os.getenv('google_api_key'))

def get_model ( ) -> GoogleGenerativeAI:
  load_env ( )
  model = GoogleGenerativeAI(
    model='models/gemini-1.5-pro-latest',
    temperature=0.5
  )
  return model

def get_embedding ( ) -> GoogleGenerativeAIEmbeddings:
  load_env ( )
  embedding = GoogleGenerativeAIEmbeddings(
    model='models/embedding-001'
  )
  return embedding 



def load_documents ( ) :
  dir_list = { dir : DATA_PATH+'\\'+dir for dir in os.listdir(DATA_PATH) }
  return dir_list


def load_contents_from_documents (dir_list : str, type_doc: str) :
  content = ''

  if type_doc == 'pdf':
    pass

  if type_doc == 'md':
    pass

  return content


  """
  

def processed_documents () -> Dict:
  # search dir documents
  

  def load_content (doc_dir:str, format:str):
    content = ''
      
    if format == 'pdf':
      # TODO obtener img 
      with open(doc_dir, 'r', encoding='ISO-8859-1') as file:
        content = file.read()  
      return content    
    
    if format == 'md':
      with open(doc_dir, 'r', encoding='utf-8') as file:
        content = file.read()

      split_by_header = content.split('#')
      split_by_header = [ c for c in split_by_header if len(c) != 0 and len(c) > 100 ]
      return split_by_header
  
  chunks = [ load_content(dir, dir.split('.')[-1]) for _,dir in doc_dirs.items()]

  return chunks


  """
