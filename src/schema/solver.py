from typing import List,Dict

from src.schema.math_model import MathModel, Expression


class Solver:
  def __init__(self,
      title:str,
      description:str,
      type:str,
      properties:Dict[str,Dict[str,str]],
      required:List[str]
    ) -> None:
    self.title = title
    self.description = description
    self.type = type
    self.properties = properties
    self.required = required
    
  def create_schema(self,
      math_models:List[MathModel],
      expressions:List[Expression]
    ) -> Dict:
    return {
      "title":self.title,
      "description":self.description.format(
        math_models,
        expressions
      ),
      "type":self.type,
      "properties":self.properties,
      "required":self.required
    }

  def __repr__(self) -> str:
    return "title: {}".format(self.title)