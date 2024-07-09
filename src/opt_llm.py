from langchain_core.messages import HumanMessage, AIMessage

from chat_history import BaseHistory

from opt_train import *
from opt_test import *

class OptimizationQ_LLM(BaseHistory):
  def __init__(self) -> None:
    super().__init__()
    self.prompt = f"""
    la definicion de un problema de optimizacion es la siguiente:

    {concepts}

    a continuacion se presentan diferentes ejemplos sobre problemas de optimizacion y sus respectivas respuestas

    eres capaz de usar lo aprendido a traves del tiempo, osea, del chat, para desarrollar mejores respuesta que le proporciones al usuario
    """
    self.chat = [
      HumanMessage(content=problem_1),
      AIMessage(content=answer_1),

      HumanMessage(content=problem_2),
      AIMessage(content=answer_2),
      
      HumanMessage(content=problem_3),
      AIMessage(content=answer_3),
      
      HumanMessage(content=problem_4),
      AIMessage(content=answer_4),
    ]

    self.make_chain()

def main():
  opt = OptimizationQ_LLM()
  response = opt.send_message(test_2)
  print(response)

if __name__ == '__main__':
  main()