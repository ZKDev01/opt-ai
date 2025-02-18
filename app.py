import json
from src.chat_history import ChatHistory
from src.schema.math_model import MathModel


INPUT_PATH = 'input.json'


def load_input () -> MathModel:
  with open(INPUT_PATH, 'r') as file:
    data = json.load(file)
  return MathModel(**data)

def main() -> None:
  math_model = load_input()
  chat = ChatHistory(temperature=0.9)
  response,attempts = chat.process_query(query=math_model, k_max=10)
  
  print(response)
  print(attempts)

if __name__ == '__main__':
  k = 5
  for _ in range(k):
    main()
  