from chat_history import BaseHistory

# Definicion de un problema de optimizacion
prompt_def_optimization = """
Un problema de optimizacion en dimension finita consiste en hallar el menor valor de la funcion f(x) si x pertenece a M,
donde M es subconjunto de R^n. Se denota:
$(P) min f(x)$
con x perteneciente a M

Se sabe que:
- $x$ es el vector formado por las variables del problema o variables de decision
- M es el conjunto de soluciones factibles 
- f(x) es la funcion objetivo 
- x* resuelve $P$ si x* pertenece a M y para todo posible valor de x en M se cumple que $f(x*) <= f(x)$
"""

# Formulacion de un modelo de programacion lineal

# Definicion del problema de asignacion de recursos
prompt_problem_asignacion_de_recursos = """
PROBLEMA: 
## Problema: Asignación de recursos
En una fábrica de cerveza se producen tres tipos distintos: rubia, negra y de baja graduación, y para ello se utilizan dos materias primas: malta y levadura. En la siguiente tabla se especifican: a) la cantidad de materias primas consumidas para producir una unidad de cada tipo de cerveza; b) las cantidades disponibles de cada materia prima; y c) el precio unitario de venta de cada tipo de cerveza

| Materia prima   | rubia | negra | baja | Disponibilidad |
| --------------- | ----- | ----- | ---- | -------------- |
| Malta           | 1     | 2     | 2    | 30             |
| Levadura        | 2     | 1     | 2    | 45             |
| Precio de venta | 7     | 4     | 3    |                |
Se trata de conocer la cantidad a fabricar de cada tipo de cerveza de manera que el beneficio sea máximo.

### Solución
Los tres elementos que definen un problema de programación lineal son: variables de decisión, restricciones y función objetivo.

**Variables de decisión**
Del enunciado del problema se desprende que las variables de decisión son las producciones a fabricar de cada tipo de cerveza:
$$begin-matrix
x_1 & = & producción de cerveza rubia 
x_2 & = & producción de cerveza negra 
x_3 & = & producción de cerveza de baja graduación  
\end-matrix$$

**Restricciones**
Las restricciones en este caso imponen que las materias primas utilizadas en la fabricación de los tres tipos de cerveza no deben sobrepasar las cantidad disponibles:
$$begin-matrix
x_1 + 2x_2 + 2x_3 \leq 30 & (malta utilizada \leq malta disponible) 
2x_1 + x_2 + 2x_3 \leq 45&(levadura utilizada \leq levadura disponible)
x_1,x_2,x_3 \geq 0      & (no negatividad) 
\end-matrix$$

**Función objetivo**
En este caso el objetivo es maximizar el beneficio, que viene dado por la suma de los precios de venta de la producción:
$$\max z = 7x_1 + 4x_2 + 3x_3$$
"""



class OptimizationQ_LLM(BaseHistory):
  def __init__(self) -> None:
    super().__init__()

    self.prompt = f"""
    Sobre la siguiente cadena responde todo lo que te pregunten

    {prompt_def_optimization}

    APRENDE A RESOLVER PROBLEMAS DE OPTIMIZACION: A continuacion se presentan diferentes ejemplos

    {prompt_problem_asignacion_de_recursos}
    
    """
    self.make_chain()

def main():
  opt = OptimizationQ_LLM()
  response = opt.send_message('Creame un problema de optimizacion con asignacion de productos con nuevos recursos, disponibilidad y diferentes precios')
  print(response)

if __name__ == '__main__':
  main()