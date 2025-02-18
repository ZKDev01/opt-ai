from typing import List,Dict



class MathModel :
  def __init__(self,
      variables:List[str],
      objetive_function:str,
      constraints:List[str],
      standard_form_model:Dict[str,str|List[str]] = {},
      possible_basic_feasible_solutions:List[List[str]] = []
    ) -> None:

    self.variables = variables
    self.objetive_function = objetive_function
    self.constraints = constraints
    self.standard_form_model = standard_form_model
    self.possible_basic_feasible_solutions = possible_basic_feasible_solutions

  def __repr__(self) -> str:
    return "MathModel(variables={}, objetive_function={}, constraints={})".format(
      self.variables, self.objetive_function, self.constraints
    )


class Expression : 
  def __init__(self,
      expression:str,
      values:Dict[str,float]
    ) -> None:
    
    self.expression:str = expression
    self.values:Dict[str,float] = values

  def __repr__(self):
    return "{} con {} se tiene evaluation={}".format(
      self.expression,self.values,self.evaluate()
    )

  def evaluate(self) -> bool:
    expr = self.expression
    for var,val in self.values.items():
      expr = expr.replace(var, str(val))
    
    try:
      result = eval(expr)
      return bool(result)
    except Exception as e:
      print(f"Error evaluating expression: {e}")
      return False

