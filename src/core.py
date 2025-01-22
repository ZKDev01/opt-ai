import os 
import io
import fitz
import dotenv
import PyPDF2
import base64


from PIL import Image
from typing import List

from langchain_google_genai import (
  GoogleGenerativeAI, 
  GoogleGenerativeAIEmbeddings
)
from langchain_core.documents import (
  Document
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
from langchain_text_splitters import (
  RecursiveCharacterTextSplitter
)
from langchain_community.document_loaders import (
  PyPDFLoader
)



# region: GLOBAL VAR
current = os.getcwd()
doc_dir = '\\database\\private'
faiss_dir = '\\faiss\\'

DATA_PATH = current + doc_dir + "\\"

CHUNK_SIZE = 1024
CHUNK_OVERLAP = CHUNK_SIZE//10

FAISS_PATH = current + faiss_dir
# endregion



def load_env ( ) -> str:
  dotenv.load_dotenv ( )
  api_key = os.environ.setdefault('google_api_key', os.getenv('google_api_key'))
  return api_key

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


def load_contents_from_documents (dir_doc : str, type_doc: str) -> List[Document] :
  dir_doc = DATA_PATH + dir_doc

  if type_doc == 'pdf':
    loader = PyPDFLoader(dir_doc,extract_images=False)
    pages = loader.load_and_split()
    return pages

  if type_doc == 'md':
    with open(dir_doc, 'r', encoding='utf-8') as file:
      content = file.read()

    split_by_header = content.split('#')
    split_by_header: List[Document] = [ Document(c) for c in split_by_header if len(c) != 0 ]
    return split_by_header

  raise Exception("formato de documento no reconocido")


def pdf_page_to_base64 (pdf_path:str, page_number:int):
  pdf_document = fitz.open(pdf_path)
  page = pdf_document.load_page(page_number)
  pix = page.get_pixmap()
  img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

  buffer = io.BytesIO()
  img.save(buffer, format="PNG")

  base64_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
  return base64_image

