from typing import Any, Dict,List

from src.vectorstore import Vectorstore
from src.data_manipulation import ExpressionsManipulation, ModelsManipulation
from src.schema.solver import Solver
from src.schema.math_model import Expression, MathModel

from langchain_core.documents import Document



class StructuredOutput:
  def __init__(self,
      model:MathModel
    ) -> None:
    self.model:MathModel = model
    self.math_models:ModelsManipulation = ModelsManipulation()
    self.expressions:ExpressionsManipulation = ExpressionsManipulation()


  def generate_new_schema (self, meta_schema:Solver, math_model:MathModel, attempts:List, k1:int=2, k2:int=10) -> Dict:
    #models:List[Document] = [ Document(page_content=str(item)) for item in self.math_models.models ]
    exprs:List[Document] = [ Document(page_content=str(item)) for item in self.expressions.expressions ]

    #vs_models:Vectorstore = Vectorstore('models',documents=models)
    vs_exprs:Vectorstore = Vectorstore('expressions',documents=exprs)

    #r1 = vs_models.search_similar_documents( query_texts=[str(math_model)], n_results=k1 )
    r2 = vs_exprs.search_similar_documents( query_texts=math_model.constraints, n_results=k2 )
    
    schema = meta_schema.create_schema(r2,attempts)
    #print(schema)
    return schema
  

  def evaluate_output(self,output:str) -> Any:
    try:
      solution = output['solution']
      exprs = [ Expression(expr,solution) for expr in self.model.constraints ]
      
      if any([ not e.evaluate() for e in exprs ]): return exprs,False
      return exprs,True
    
    except Exception as e:
      print( "-error al evaluar la salida-" )
      return [],False

