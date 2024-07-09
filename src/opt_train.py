

concepts = """
un problema de optimizacion en dimension finita consiste en hallar el menor o mayor valor de una funcion f(x) si x pertenece a M, 
donde M es el subconjunto de soluciones factibles

min f(x) o max f(x)

- se sabe que f(x) es la funcion objetivo
- se sabe que x es un vector formado por las variables del problema o variables de decision
- se sabe que un problema de programacion lineal contiene lo que se denominan como restricciones.

las restricciones son funciones g(x) o h(x) tales que g(x) < 0, g(x) > 0, g(x) >= 0, g(x) <= 0, mientras que h(x) = 0.
g(x) representan las inecuaciones que tienen que cumplirse para que f(x) sea minima o maxima
h(x) representan las ecuaciones que tienen que cumplirse para que f(x) sea minimia o maxima 
"""


problem_1 = """ 
example input: 

el problema siguiente es de asignacion de recursos y consiste: en una fábrica de cerveza se producen tres tipos distintos: rubia, negra y de baja graduación, y para ello se utilizan dos materias primas: malta y levadura 
en la siguiente tabla se especifican: 

- la cantidad de materias primas consumidas para producir una unidad de cada tipo de cerveza; 
- las cantidades disponibles de cada materia prima; y c) el precio unitario de venta de cada tipo de cerveza

se trata de conocer la cantidad a fabricar de cada tipo de cerveza de manera que el beneficio sea máximo.

tabla
| materia prima   | rubia | negra | baja | disponibilidad |
| --------------- | ----- | ----- | ---- | -------------- |
| malta           | 1     | 2     | 2    | 30             |
| levadura        | 2     | 1     | 2    | 45             |
| precio de venta | 7     | 4     | 3    |                |

respuesta al problema:

variables de decision: del enunciado del problema se desprende que las variables de decisión son las producciones a fabricar de cada tipo de cerveza:

x_1 : produccion de cerveza rubia
x_2 : produccion de cerveza negra
x_3 : produccion de cerveza de baja graduacion

restricciones:

Las restricciones en este caso imponen que las materias primas utilizadas en la fabricación de los tres tipos de cerveza no deben sobrepasar las cantidad disponibles:
  x_1 + 2x_2 + 2x_3 <= 30 (Malta utilizada <= Malta disponible)
  2x_1 + x_2 + 2x_3 <= 45 (Levadura utilizada <= Levadura disponible)  

Las restricciones que garantizan la no negatividad de las variables de decision son:
  x_1 >= 0
  x_2 >= 0
  x_3 >= 0

funcion objetivo:
En este caso el objetivo es maximizar el beneficio, que viene dado por la suma de los precios de venta de la producción:
max z = 7x_1 + 4x_2 + 3x_3
"""



problem_2 = """
example input: 

en una fábrica se producen n tipos distintos de productos, y para ello se utilizan m recursos. 
en la siguiente tabla se especifican: 

se trata de conocer la cantidad a fabricar de cada tipo de producto de manera que el beneficio sea máximo.

tabla
| recursos                                 | 1    | 2    | ... | n    | cantidad de recursos disponibles  |
| ---------------------------------------- | ---- | ---- | --- | ---- | --------------------------------- |
| 1                                        | c_11 | c_12 | ... | a_1n | b_1                               |
| 2                                        | c_21 | c_22 | ... | a_2n | b_2                               |
| ...                                      | ...  | ...  | ... | ...  | ...                               |
| m                                        | c_m1 | c_m2 | ... | c_mn | b_m                               |
| contribucion a z por unidad de actividad | c_1  | c_2  | ... | c_n  |                                   |

respuesta al problema:

variables de decision:

z = valor del rendimiento
x_j = nivel de la actividad j (para j = 1,2,...,n)
c_j = incremento en z que se obtiene al aumentar una unidad el nivel de la actividad j
b_i = cantidad de recurso i disponible para asignarse a las actividades (para i = 1,2,...,n)
a_ij = cantidad del recurso i consumido por cada unidad de la actividad j

restricciones:

a_11 * x_1 + a_12 * x_2 + ... + a_1n * x_n <= b_1 
a_21 * x_1 + a_22 * x_2 + ... + a_2n * x_n <= b_2 
...
a_m1 * x_1 + a_m2 * x_2 + ... + a_mn * x_n <= b_m 
x_1 >= 0
x_2 >= 0
...
x_n >= 0

funcion objetivo:

max z = c_1 * x_1 + c_2 * x_2 + ... + c_n * x_n
"""



