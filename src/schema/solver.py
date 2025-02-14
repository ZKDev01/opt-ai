from typing import List

class Solver:
  def __init__(self, few_shots:List[str]) -> None:
    ...
    self.json_schema:str = "..."

  def get_schema(self) -> str:
    return self.json_schema

