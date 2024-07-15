# The next code is for only test method 
from langchain_core.prompts import ChatPromptTemplate

from src.chat_history import BaseHistory
from src.tot_opt import get_answer_from_tot
from src.tools import get_model
from src.primary_process_engine import selector_system


def main() -> None:
  historial = BaseHistory()
  query = 'hola mundo'
  output = selector_system ( llm_historial = historial, query = query )
  print(output)


if __name__ == '__main__':
  main()
