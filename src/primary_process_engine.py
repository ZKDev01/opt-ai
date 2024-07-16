from langchain_core.prompts import ChatPromptTemplate

from src.chat_history import BaseHistory
from src.cot_opt import get_answer_from_cot
from src.tools import get_model

from src.opt.mixing_problem import mixing_general, mixing_examples


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



def input_to_apply_rag (input: str, kvalues: int = 5):
  pass

def input_like_mixing_problem (input: str, ksolutions: int = 5) -> str:
  
  req = {
    'INPUT' : input,
    'NUMBERS_OF_SOLUTIONS' : ksolutions,
    'TYPE' : 'problema de la mezcla o mixing problem',
    'GENERAL' : mixing_general,
    'EXAMPLES' : mixing_examples
  }

  answer = get_answer_from_cot(req=req)

  return answer

def input_like_personnel_scheduling_1 (input: str) -> str:
  pass

def input_like_personnel_scheduling_2 (input: str) -> str:
  pass

def input_like_resource_allocation (input: str) -> str:
  pass




