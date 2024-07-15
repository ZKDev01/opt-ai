from langchain_core.prompts import ChatPromptTemplate

from src.chat_history import BaseHistory
from src.tot_opt import get_answer_from_tot
from src.tools import get_model


rag_prompt = """
PREPARATION: 
- Debes ser capaz de responder a la respuesta segun el contenido de DOCUMENTS que se te presenten de la mejor forma posible
- Si el contenido de DOCUMENTS no aporta informacion para responder la pregunta, entonces ignora la pregunta y el contenido presentado y no respondas. Responde que no eres capaz de responder dicha pregunta
    
OUTPUT FORMAT:
- La respuesta debe contener dos campos: RESPUESTA, NEW_DOCUMENTS
  - RESPUESTA: Respuesta a la pregunta usando el contenido presentado
  - USED DOCUMENTS: Resumen de las ideas que se tomaron de los contenidos de DOCUMENTS presentados

INTERACTION EXAMPLES: Un ejemplo es el siguiente:
```
DOCUMENTS: 
'Los LLM se entrenan con grandes volúmenes de datos y usan miles de millones de parámetros para generar resultados originales en tareas como responder preguntas, traducir idiomas y completar frases.'
QUESTION: 
'Que es un LLM?'
OUTPUT:
  RESPUESTA POSIBLE: Los LLM son entrenados con grandes volumenes de datos para generar resultados originales 
  USED DOCUMENTS: 'Los LLM se entrenan con grandes volúmenes de datos para generar resultados originales en tareas como responder preguntas y completar frases.'
```

=========================
DOCUMENTS: 
  {results}
QUESTION: {message}

OUTPUT:
  RESPUESTA POSIBLE: 
  USED DOCUMENTS: 
"""



def selector_system (llm_historial: BaseHistory, query: str, kvalues_for_rag: int = 5, numbers_througth: int = 5) -> str:
  model = get_model()
  prompt = ChatPromptTemplate.from_messages([
    ('human', """
      Puedes identificar que tipo de prompt elegir en consecuencia del input del usuario:

      INPUT: {query}

      Puedes determinar si el input es:
        OPT -> problema de optimizacion
        RAG -> pregunta que debe ser respondida usando la tecnica de Generacion Mejorada de Informacion 
    
      OUTPUT
      """ )
    ])

  chain = prompt | model

  answer = chain.invoke( { 
    'query': query  
  } )

  return answer


def selector_with_llm ():
  pass


def selector_optimization_problem (input: str) -> list[str]:
  prompt = f"""
  Eres un asistente capaz de seleccionar, dado un problema de optimizacion,
  otro problema que pueda ser capaz de parecerse. 

  -----------------------------------------------------

  Problemas con su descripcion:
  
  ASIGNACION DE RECURSOS:  
    NOMBRE:         asignacion de recursos
    DESCRIPCION:    [DESCRIPCION]
  
  CAMINANTE: 
    NOMBRE:         caminante
    DESCRIPCION:    [DESCRIPCION]
    
  PERSONAL SCHEDULING: 
    NOMBRE:         problema del caminante
    DESCRIPCION:    [DESCRIPCION] 
  
  -----------------------------------------------------
  
  Posibles output: 
    PROBLEM TYPE:   NOMBRE de algun tipo de problema presentado anteriormente
    DESCRIPTION:    DESCRIPCION del problema 
    INPUT:          Entrada que se analizo / Problema original 
  
  -----------------------------------------------------
  
  INPUT: {input}  
  """

  pass


