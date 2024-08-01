from src.tools import get_model

from langchain_core.messages import HumanMessage, AIMessage

from langchain.chains.llm import LLMChain
from langchain.chains.sequential import SequentialChain
from langchain.prompts import PromptTemplate

from src.chat_history import BaseHistory

class COT_history:
  def __init__(self, general: str, examples: str) -> None:
    self.examples = examples
    self.historial = BaseHistory (with_vectorstore=False)
    self.historial.prompt = f"""
    Eres capaz de resolver problemas de optimizacion especificos y utilizar la conversacion que tengas con el usuario para aprender 

    Tienes la capacidad de responder los problemas con una estructura de 
    - Variables de decision: variables que permiten identificar el modelo propuesto 
    - Restricciones: ecuaciones o inecuaciones que restrigen las opciones de las variables de decision
    - Funcion objetivo: esta es una funcion a maximizar o minimizar que cumpla con el problema de optimizacion especificado
    
    El problema general que puedes responder es: 
    {general}
    """
    self.clean_history()
    self.historial.make_chain()

  def clean_history (self) -> None:
    self.chat = [
      HumanMessage(f"Puedes usar los siguientes ejemplos para que devuelvas mejores respuestas: {self.examples}")
    ]

  def send_processed_input(self, input: str) -> str:
    response = self.historial.chain.invoke( { 'input': input, 'chat': self.chat } )
    return response


  def cot_processed_problem (self, problem: str, kvalues: int = 3) -> list[str]:
    proposed_result = []
    
    for _ in range(1,kvalues+1):
      tmp = self.send_processed_input( input=f"""
      Resuelve el problema de optimizacion siguiente: {problem}

      La propuesta que me des debe ser diferente a las siguientes:
      {proposed_result}
      """ )
      proposed_result.append(tmp)

    evaluate_result = []

    for proposed in proposed_result:
      tmp_evaluate = self.send_processed_input( input=f"""
      Analiza el siguiente problema de optimizacion: {problem}

      Analiza ahora la siguiente propuesta: {proposed}

      Determina de la propuesta anterior: 
      - Ventajas del modelo propuesta como solucion del problema de optimizacion
      - Desventajas que puede tener el modelo
      - Fallos que puede presentar 
      - Asigna una probabilidad de exito ante el problema
      """ )

      tmp_final = self.send_processed_input ( input=f"""
      SOLUCION: {proposed}

      EVALUACION DE LA SOLUCION: {tmp_evaluate}

      Clasifique la solucion basandose en la evaluacion siguiente y asigna una posibilidad de exito 
      Proporcione una justificacion y pensamientos finales para la clasificacion. 
      
      Esta clasificacion debe desglosarse en 4 puntos:
      - Probabilidad de exito
      - Justificacion
      - Modos de fallo
      - Pensamientos finales
      """ )

      evaluate_result.append(tmp_final)

    return evaluate_result

