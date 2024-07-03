from chat_history import BaseHistory

# DEFINICIONES SOBRE PROBLEMAS DE OPTIMIZACION
optimization = """
Un problema de optimizacion en dimension finita consiste en hallar el menor valor de la funcion f(x) si x pertenece a M,
donde M es subconjunto de R^n. Se denota:
$(P) min f(x)$
con x perteneciente a M

Se sabe que:
- $x$ es el vector formado por las variables del problema o variables de decision
- M es el conjunto de soluciones factibles 
- f(x) es la funcion objetivo 
- x* resuelve $P$ si x* pertenece a M y para todo posible valor de x en M se cumple que $f(x*) <= f(x)$

Los tres elementos que definen una solucion a un problema de programación lineal son: variables de decisión, restricciones y función objetivo.
"""

# PROBLEMA: ASIGNACION DE RECURSOS
problem_1 = """
PROBLEMA: Asignación de recursos

DESCRIPCION:
En una fábrica de cerveza se producen tres tipos distintos: rubia, negra y de baja graduación, y para ello se utilizan dos materias primas: malta y levadura. En la siguiente tabla se especifican: 
a) la cantidad de materias primas consumidas para producir una unidad de cada tipo de cerveza; 
b) las cantidades disponibles de cada materia prima; y c) el precio unitario de venta de cada tipo de cerveza
Se trata de conocer la cantidad a fabricar de cada tipo de cerveza de manera que el beneficio sea máximo.

TABLA:
| Materia prima   | rubia | negra | baja | Disponibilidad |
| --------------- | ----- | ----- | ---- | -------------- |
| Malta           | 1     | 2     | 2    | 30             |
| Levadura        | 2     | 1     | 2    | 45             |
| Precio de venta | 7     | 4     | 3    |                |

VARIABLES DE DECISION:
Del enunciado del problema se desprende que las variables de decisión son las producciones a fabricar de cada tipo de cerveza:

x_1 : produccion de cerveza rubia
x_2 : produccion de cerveza negra
x_3 : produccion de cerveza de baja graduacion

RESTRICCIONES:
Las restricciones en este caso imponen que las materias primas utilizadas en la fabricación de los tres tipos de cerveza no deben sobrepasar las cantidad disponibles:
  x_1 + 2x_2 + 2x_3 <= 30 (Malta utilizada <= Malta disponible)
  2x_1 + x_2 + 2x_3 <= 45 (Levadura utilizada <= Levadura disponible)  

Las restricciones que garantizan la no negatividad de las variables de decision son:
  x_1 >= 0
  x_2 >= 0
  x_3 >= 0

FUNCION OBJETIVO:
En este caso el objetivo es maximizar el beneficio, que viene dado por la suma de los precios de venta de la producción:
max z = 7x_1 + 4x_2 + 3x_3
"""

# PROBLEMA GENERALIZADO: ASIGNACION DE RECURSOS
problem_2 = """
PROBLEMA: Asignación de recursos generalizado

DESCRIPCION:
En una fábrica se producen n tipos distintos de productos, y para ello se utilizan m recursos. En la siguiente tabla se especifican: 

Se trata de conocer la cantidad a fabricar de cada tipo de producto de manera que el beneficio sea máximo.

TABLA:
| Recursos                                 | 1   | 2   | ... | n   | Cantidad de recursos disponibles |
| ---------------------------------------- | --- | --- | --- | --- | -------------------------------- |
| 1                                        | c11 | c12 | ... | a1n | b1                               |
| 2                                        | c21 | c22 | ... | a2n | b2                               |
| ...                                      | ... | ... | ... | ... | ...                              |
| m                                        | cm1 | cm2 | ... | cmn | bm                               |
| Contribucion a z por unidad de actividad | c1  | c2  | ... | cn  |                                  |

VARIABLES DE DECISION:

  z = valor del rendimiento
  xj = nivel de la actividad j (para j = 1,2,...,n)
  cj = incremento en z que se obtiene al aumentar una unidad el nivel de la actividad j
  bi = cantidad de recurso $i$ disponible para asignarse a las actividades (para i = 1,2,...,n)
  aij = cantidad del recurso i consumido por cada unidad de la actividad j

RESTRICCIONES:
a11 * x1 + a12 * x2 + ... + a1n * xn <= b1 
a21 * x1 + a22 * x2 + ... + a2n * xn <= b2 
...
am1 * x1 + am2 * x2 + ... + amn * xn <= bm 
x1 >= 0
x2 >= 0
...
xn >= 0

FUNCION OBJETIVO:
max z = c1 * x1 + c2 * x2 + ... + cn * xn
"""

# PROBLEMA DEL VIAJANTE


class OptimizationQ_LLM(BaseHistory):
  def __init__(self) -> None:
    super().__init__()
    self.prompt = f"""
    Eres una IA capaz de resolver problemas de optimizacion
    Puedes usar los siguientes ejemplos para encontrar respuestas adecuadas a la definicion de los problemas que se te presenten. 
    Si no puedes usar estos problemas para encontrar una respuesta entonces, sin salir de la area que se te especifico, da una solucion factible basandote en los conceptos definidos

    CONCEPTOS SOBRE OPTIMIZACION
    {optimization}
    
    EJEMPLOS DE PROBLEMAS DE OPTIMIZACION RESUELTOS:
    {problem_1}
    {problem_2}
    """

    self.make_chain()

testing_1 = """
Una empresa se dedica a producir dos tipos de folletos: blancos, negros, y para ello se utilizan 3 tipos de recursos: papel, color negro, color blanco, sello de tipo 1, sello de tipo 2  

Se presenta a continuacion una tabla para resolver el problema:

| Recursos        | Folleto blanco | Folleto negro | Cantidad en la empresa para la produccion |
| --------------- | -------------- | ------------- | ----------------------------------------- |
| Papel           | 1              | 2             | 100                                       |
| Color negro     | 4              | 3             | 200                                       |
| Color blanco    | 3              | 5             | 200                                       |
| Sello de tipo 1 | 7              | 5             | 250                                       |
| Sello de tipo 2 | 4              | 8             | 250                                       |
| Precio de venta | 15             | 20            |                                           |

Se desea conocer la cantidad a fabricar de cada tipo de producto de manera que el beneficio sea máximo
"""

testing_2 = "Desarrollame un problema de asignacion"

def main():
  opt = OptimizationQ_LLM()
  response = opt.send_message(testing_2)
  print(response)

if __name__ == '__main__':
  main()