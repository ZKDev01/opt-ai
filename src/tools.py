import os
import dotenv

from langchain_google_genai import GoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field



def load_environment():
  """
  Carga las variables de entorno necesarias para el funcionamiento del programa

  Esta funcion utiliza la biblioteca `dotenv` para cargar variables de entorno desde un archivo `.env`

  Especificamente buscar las variables de entorno siguientes:
  - `google_api_key` : clave de API de Google  
  """

  dotenv.load_dotenv()
  os.environ.setdefault('google_api_key', os.getenv('google_api_key'))



def get_model() -> GoogleGenerativeAI:
  """
  Inicializa y devuelve una instancia de GoogleGenerativeAI
  con configuraciones predeterminadas 

  Contiene una funcion para cargar las credenciales de Google API 
  desde el entorno y crea una instancia de GoogleGenerativeAI
  usando el modelo 'gemini-1.5-pro'

  Args:

  Returns:
      GoogleGenerativeAI: instancia preconfigurada de GoogleGenerativeAI
  """

  load_environment()
  model = GoogleGenerativeAI(
    model='models/gemini-1.5-pro-latest',
    temperature=0.5
  )
  return model



def get_embedding() -> GoogleGenerativeAIEmbeddings:
  """
  Inicializa y devuelve una instancia de `GoogleGenerativeAIEmbeddings`

  Esta funcion carga las credenciales de Google API desde el entorno y crea una instancia de `GoogleGenerativeAIEmbeddings`

  Returns:
      GoogleGenerativeAIEmbeddings: instancia preconfigurada del embedding model 
  """

  load_environment()
  embedding = GoogleGenerativeAIEmbeddings(
    model='models/embedding-001'
  )
  return embedding 



def prompt_template_QA(question: str, k: int, model: GoogleGenerativeAI) -> str:
  """
  Este metodo construye un template de chat que incluye instrucciones claras para el modelo de IA sobre como responder 
  a una pregunta especifica y sugerir posibles preguntas relacionadas. 

  Utiliza parametro `k` para especificar la cantidad de recomendaciones de preguntas debe incluir en su respuesta

  Args:
      question (str): la pregunta especifica que se desea que el modelo responda 
      k (int): cantidad de recomendaciones de preguntas relacionadas que se deben incluir en la respuesta 
      model (GoogleGenerativeAI): instancia del modelo de IA utilizado para generar respuesta

  Returns:
      result (str): respuesta generada por el modelo, incluyendo tanto la respuesta directa a la pregunta como las recomendaciones de preguntas relacionadas
      
  """

  prompt = ChatPromptTemplate.from_template(
    """ 
    Se lo mas simple posible para responder la siguiente pregunta 
    y da algunas recomendaciones a preguntas que se parezcan al tema de la pregunta

    Solo devuelve la respuesta. Seguido de las preguntas. Ejemplo:
    
    Answer

    Posibles preguntas:
    - Pregunta sugerida 1
    - Pregunta sugerida 2
    - Pregunta sugerida 3  

    El numero de preguntas que sugieres debe estar fijado al siguiente numero:
    Numero de recomendaciones: {k}

    Q: {question}
    A: 
    """
  )
  
  chain = prompt | model 
  result = chain.invoke(
    {
      "question": question,
      "k": k
    })
  return result



def prompt_template_json_example_person(message: str, model: GoogleGenerativeAI) -> str:
  """
  Construye y ejecuta un prompt basado en un mensaje dado, utilizando un formato especifico para extraer informacion relevante.
  Este metodo utiliza un ChatPromptTemplate para guiar la respuesta del modelo de IA, esperando recibir datos en un formato JSON especifico


  Args:
      message (str): mensaje o entrada inicial que se utilizara como base para extraer informacion
      model (GoogleGenerativeAI): instancia del modelo de IA que procesara el prompt y generara la respuesta

  Returns:
      str: cadena de texto que contiene la respuesta del modelo, procesada segun el formato JSON especificado en el prompt
  """

  prompt = ChatPromptTemplate.from_messages([
    ("system", "Extrae informacion de la siguiente frase. Siguiendo este formate {format}"),
    ("human", "{message}")
  ])

  class Person(BaseModel):
    name: str = Field(description="nombre de la persona")
    age: int = Field(description="edad de la persona")

  parser = JsonOutputParser(pydantic_object=Person)
  chain = prompt | model | parser

  result = chain.invoke({
    "format": parser.get_format_instructions(),
    "message": message
  })
  return result



def prompt_template_parser_string(question: str, model: GoogleGenerativeAI) -> str:
  """
  Responde una pregunta especifica utilizando un modelo de LLM. 

  Contiene un parser para convertir la salida a str

  Args:
      question (str): la pregunta especifica a la que se desea que el modelo responda 
      model (GoogleGenerativeAI): instancia del LLM utilizado para generar la respuesta

  Returns:
      str: respuesta generada por el LLM a la pregunta 
  """

  prompt = ChatPromptTemplate.from_template("Responde a la pregunta de la forma mas simple: {question}")
  parser = StrOutputParser()

  chain = prompt | parser | model
  result = chain.invoke({"question": question})
  
  return result



def prompt_template_parser_list_simility(word: str, k: int, model: GoogleGenerativeAI) -> str:
  """
  Genera una lista de sinonimos para una palabra dada utilizando un LLM

  Esta funcion construye un template de chat que solicita al LLM generar una lista de sinonimos. 
  La cantidad especifica de sinonimos esta dada por un parametro k

  Args:
      word (str): la palabra para la cual se buscaran sinonimos
      k (int): numero de sinonimos que se desea obtener
      model (GoogleGenerativeAI): instancia del modelo de lenguaje AI utilizada para generar la respuesta

  Returns:
      str: una cadena de texto conteniendo los simbolos de la palabra dada, separados por comas
  """
  prompt = ChatPromptTemplate.from_template("Dime {k} sinonimos de: {word} \\La respuesta debe tener los sinonimos separados por coma")
  parser = CommaSeparatedListOutputParser()

  chain = prompt | parser | model
  result = chain.invoke({
    "word": word,
    "k": k
  })
  
  return result


