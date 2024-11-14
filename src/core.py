import os 
import dotenv

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
