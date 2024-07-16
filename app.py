# The next code is for only test method 
from langchain_core.prompts import ChatPromptTemplate

from src.chat_history import BaseHistory
from src.tools import get_model
from src.primary_process_engine import input_to_apply_rag, input_like_mixing_problem

def testing_rag() -> str:
  pass



def testing_mixing_problem() -> str:
  input = """
  una fábrica produce combustible mezclando diferentes materiales: material A, material B, material C, material D, material E 
  en un mes sólo entra en la fabrica 100 toneladas de materiales A, B, C, D, mientras que del material E entran 150 toneladas 
  el combustible resultante debe cumplir un valor de dureza comprendido entre 10 y 20
  el costo de una tonelada para cada combustible mezclado junto con su dureza aparecen en la siguiente tabla:

|        | material A  | material B  | material C  | material D  | material E  |
| ------ | ----------- | ----------- | ----------- | ----------- | ----------- |
| costo  | 190         | 215         | 230         | 200         | 130         |
| dureza | 11.0        | 9.9         | 12.1        | 14.0        | 10.9        |

  se trata de refinar las cantidades apropiadas de cada material a fin de maximizar el beneficio de la producción final sabiendo que una tonelada del combustible producido se vende a 300

  """

  answer = input_like_mixing_problem(input=input, ksolutions=6)
  return answer 



def main() -> None:
  historial = BaseHistory()
  query = 'hola mundo'

  print(query)


if __name__ == '__main__':
  print ( testing_mixing_problem() )

