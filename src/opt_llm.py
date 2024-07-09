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

    tu respuesta final debe estar contenida en: 'respuesta al problema:'
    """
    
    self.chat = [problem_1, problem_2]

    self.make_chain()

def main():
  opt = OptimizationQ_LLM()
  response = opt.send_message(f'Resuelve el siguiente problema: {test_1}')
  print(response)

if __name__ == '__main__':
  main()