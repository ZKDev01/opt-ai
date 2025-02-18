from ast import expr
import json
from typing import List,Dict

from src.schema.math_model import MathModel,Expression


MODELS_PATH = 'data/opt/math_models.json'
EXPRESSIONS = 'data/opt/expressions.json'
PROMPTS_PATH = 'data/prompts/opt_prompts.json'


class ModelsManipulation:
  models:List[MathModel] 

  def __init__(self) -> None:  
    self.read()
  
  def read (self) -> None:
    with open(MODELS_PATH, 'r') as file:
      data = json.load(file)
    self.models = [ MathModel(**item) for item in data['models'] ]

  def add (self,model:MathModel) -> None:
    self.models.append(model)
    self.update_json()

  def delete (self,position:int) -> None:
    self.models.pop(position)
    self.update_json()

  def update_json(self) -> None:
    with open(MODELS_PATH, 'w') as file:
      data = { 'models': [ model.__dict__ for model in self.models ] }
      json.dump(data,file)

class ExpressionsManipulation:
  expressions:List[Expression]

  def __init__(self):
    self.read()

  def read (self) -> None:
    with open(EXPRESSIONS, 'r') as file:
      data = json.load(file)
    self.expressions = [ Expression(**item) for item in data['expressions'] ]
  
  def add (self,expression:Expression) -> None:
    try:
      expression.evaluate()
      self.expressions.append(expression)
      self.update_json()
    except Exception as e:
      print(f"Fail in add Expression: {expression}")
  
  def delete (self,position:int) -> None:
    self.expressions.pop(position)
    self.update_json()

  def clean_expressions(self) -> None:
    #print(len(self.expressions))
    expr = { str(e) : e for e in self.expressions }
    self.expressions = [ v for k,v in expr.items() ]
    #print(len(self.expressions))

  def update_json(self) -> None:
    self.clean_expressions()
    with open(EXPRESSIONS, 'w') as file:
      data = { 'expressions': [ expr.__dict__  for expr in self.expressions] }
      json.dump(data,file)




def load_prompts () -> Dict[str,Dict]:
  with open(PROMPTS_PATH, 'r') as file:
    data = json.load(file)
  prompts:Dict[str,Dict] = {
    'meta-basic-solver': data['meta-basic-solver']
  }
  return prompts

