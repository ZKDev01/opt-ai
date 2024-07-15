# The next code is for only test method 
from langchain_core.prompts import ChatPromptTemplate

from src.chat_history import BaseHistory
from src.tot_opt import get_answer_from_tot
from src.tools import get_model
from src.primary_process_engine import input_to_apply_rag


def main() -> None:
  historial = BaseHistory()
  query = 'hola mundo'

  print(query)


if __name__ == '__main__':
  main()
