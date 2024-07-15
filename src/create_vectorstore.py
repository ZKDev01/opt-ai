from typing import List
from src.tools import get_model, get_embedding
import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document

model = get_model()
embedding = get_embedding()

current = os.getcwd()
doc_dir = '\\database\\doc'
faiss_dir = '\\database\\faiss'

DATA_PATH = current + doc_dir
FAISS_PATH = current + faiss_dir

dir = os.listdir(DATA_PATH)

def search_docs() -> list[str]:
  """
  Busca todos los documentos disponibles en el directorio especificado y retorna sus rutas completas

  Este metodo recorre el directorio establecido en la variable global 'DATA_PATH', buscando todos los archivos presentes y retornando sus rutas completas como una lista de cadenas
  
  Nota: Las rutas devueltas son relativas al directorio actual del proyecto

  Returns:
      list[str]: una lista de cadenas donde cada elemento es la ruta completa de un documento encontrado en el directorio especificado
  """
  docs_dir = os.listdir(DATA_PATH)
  docs_dir = [DATA_PATH + '\\' + item for item in docs_dir]
  return docs_dir

def load_contents(docs_dir: list[str]) -> list[str]:
  """
  Lee y retorna el contenido de todos los documentos especificados por sus rutas.

  Este metodo itera sobre cada ruta del documento proporcionada en la lista 'docs_dir', lee el contenido de cada uno de estos archivos y los agrega a una lista, la cual luego retorna

  Nota: Los archivos deben estar en formato de texto plano para poder ser leidos correctamente por este metodo

  Args:
      docs_dir (list[str]): Lista de rutas de directorios completas a los documentos cuyo contenido se desea leer

  Returns:
      list[str]: Lista de cadenas donde cada elemento es el contenido leido de un documento correspondiente a las rutas proporcionadas
  """

  def load_content(doc_dir: str):
    content = ''
    with open(doc_dir, 'r', encoding='ISO-8859-1') as file:
      content = file.read()
    return content  
  
  docs_content = [load_content(doc_dir=doc_dir) for doc_dir in docs_dir]
  return docs_content 

def chunkenizer(content: str) -> List[Document]:
  """
  Este metodo se encarga de separar en chunks el contenido de un documento. Esta fragmentacion la hace usando un metodo recursivo llamado `RecursiveCharacterTextSplitter` con valores predeterminados

  Args:
      content (str): contenido de un documento correspondiente

  Returns:
      List[Document]: lista de chunks del documento de entrada 
  """

  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1024,
    chunk_overlap = 204,
    length_function = len
  )
  chunks = text_splitter.create_documents([content])
  return chunks

def create_chunks() -> List[Document]:
  """
  Divide el contenido de todos los documentos encontrados en chunks. 

  Este metodo primero busca todos los documentos disponibles en el directorio especificado, 
  luego lee y retorna el contenido de estos documentos. Posteriormente, divide el contenido de cada documento
  en chunks utilizando un metodo especifico de division de texto, y retorna una lista de objetos `Document`, 
  donde cada objeto representa un chunk del contenido original

  Returns:
      List[Document]: Una lista de objetos Document, donde cada objeto representa un chunk del contenido de un documento
  """

  docs_dir = search_docs()
  docs_content = load_contents(docs_dir)
  chunks: List[Document] = []
  for doc_content in docs_content:
    
    document = Document(page_content=doc_content)
    chunks.append(document)
    
    """ 
    # CHUNK THE DOCUMENTS
    for item in chunkenizer(doc_content):
      chunks.append(item)
    """
    
  return chunks

class FAISS_VECTORSTORE():

  def __init__(self, load: bool = False) -> None:
    """
    Inicializa una instancia de `FAISS_VECTORSTORE` para manejar y buscar en una base de datos vectorial de FAISS

    Este constructor permite opcionalmente cargar la base de datos vectorial existente si se pasa `True` al parametro `load`. 
    Si `load` es `False` (valor predeterminado), se crea una nueva base de datos vectorial con los documentos proporcionados

    Args:
        load (bool, optional): Indica si se debe cargar la base de datos vectorial. Defaults to False.
    """
    if load: 
      self.__vs = FAISS.load_local(
        folder_path=FAISS_PATH, 
        embeddings=embedding,
        allow_dangerous_deserialization=True)
    else:
      chunks = create_chunks()
      
      """ 
      ERROR POR LA CANTIDAD DE ELEMENTOS DE CHUNKS (debe ser por eso)
      self.__vs = FAISS.from_documents(
        documents=chunks,
        embedding=embedding
      )
      """

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
    """
    Realiza una busqueda de similaridad en la base de datos vectorial utilizando una consulta 

    Este metodo busca en los documentos, los similares a la consulta proporcionada, utilizan el numero de resultados `k`

    Args:
        query (str): la consulta de texto para realizar la busqueda de similitud
        k (int, optional): numero de resultados similares a retornar. Defaults to 3.

    Returns:
        list[str]: una lista de cadenas donde cada elemento es el contenido de un documento encontrado que es similar a la consulta
    """
    if not k > 0:
      raise Exception("k no puede ser negativo ni 0")
    results = self.__vs.similarity_search(query=query, k=k)
    results_content = [result.page_content for result in results]
    return results_content

class MONGODB_VECTORSTORE():
  # TODO
  pass

def testing_create_vectorstore():
  FAISS_VECTORSTORE()

def testing_load_and_query_something():
  vs = FAISS_VECTORSTORE(load=True)
  result = vs.similarity_search(query='que es la apologetica', k=10)
  for item in result:
    print(item)

if __name__ == "__main__":
  testing_create_vectorstore()
  testing_load_and_query_something()
  