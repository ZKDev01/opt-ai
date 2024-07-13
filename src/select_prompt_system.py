

def selector_system (input: str) -> str:

  prompt = f"""

  Posibles respuestas: (devuelve solo uno) 
  - 'PROBLEMA DE OPTIMIZACION'
  - 'RAG'
  """
  
  answer = ''

  # SELECCIONAR ENTRE LOS PROMPT DE TOT DE OPT
  if answer == 'PROBLEMA DE OPTIMIZACION':
    return selector_optimization_problem(input=input) 

  # SELECCIONAR ENTRE RAG  
  if answer == 'RAG':
    return 

  





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


