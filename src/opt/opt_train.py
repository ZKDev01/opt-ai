

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







problem_3 = """ 
una fábrica produce aceite mezclando aceites refinados, dos de origen vegetal y tres de origen no vegetal 
en un mes sólo es posible refinar 200 toneladas de vegetal y 250 de no vegetal 
el aceite resultante debe cumplir un valor de dureza comprendido entre 3 y 6 
el costo de una tonelada para cada aceite refinado junto con su dureza aparecen en la siguiente tabla:

|        | Veg_1     | Veg_2     | NoVeg_1     | NoVeg_2     | NoVeg_3     |
| ------ | --------- | --------- | ----------- | ----------- | ----------- |
| costo  | 110       | 120       | 130         | 110         | 115         |
| dureza | 8.8       | 6.1       | 2.0         | 4.2         | 5.0         |

se trata de refinar las cantidades apropiadas de cada aceite a fin de maximizar el beneficio de la producción final sabiendo que una tonelada del aceite producido se vende a 150
"""

answer_3 = """ 
**variables de decision**

  x_1: cantidad de aceite refinado Veg_1
  x_2: cantidad de aceite refinado Veg_2
  x_3: cantidad de aceite refinado NoVeg_1
  x_4: cantidad de aceite refinado NoVeg_2
  x_5: cantidad de aceite refinado NoVeg_3
  y: cantidad de aceite a producir

**restricciones**

aceite no vegetal refinado <= capacidad de refino vegetal
  x_1 + x_2 <= 200 

aceite no vegetal refinado <= capacidad de refino no vegetal
  x_3 + x_4 + x_5 <= 250   

límite superior de dureza del aceite producido
  8.8 * x_1 + 6.1 * x_2 + 2 * x_3 + 4.2 * x_4 + 5 * x_5 <= 6 * y 

límite inferior de dureza del aceite producido  
  8.8 * x_1 + 6.1 * x_2 + 2 * x_3 + 4.2 * x_4 + 5 * x_5 >= 3 * y   

suma de las cantidades de los aceites refinados = cantidad de aceite producido
  x_1 + x_2 + x_3 + x_4 + x_5 = y 

no negatividad
  x_1 >= 0
  x_2 >= 0
  x_3 >= 0
  x_4 >= 0
  x_5 >= 0
  x_6 >= 0

**funcion objetivo**

max z = 150 * y - 110 * x_1 - 120 * x_2 - 130 * x_3 - 110 * x_4 - 115 * x_5
"""


problem_4 = """ 
una compañía monta un sistema de producción en un proceso dividido en 4 tareas denominadas M, N, P y Q que pueden realizarse en cualquier orden e indistintamente por 4 equipos. 
en la siguiente tabla aparecen: 
a) el tiempo en horas que emplearía cada equipo en realizar la tarea completa; 
b) las horas disponibles por cada equipo; y 
c) el coste de la hora de trabajo de cada equipo. 
se quiere conocer el número de horas de trabajo que deben asignarse a cada equipo para que se minimice el coste total del montaje del sistema.

| Equipo | M   | N   | P   | Q   | Horas disponibles | Coste/hora |
| ------ | --- | --- | --- | --- | ----------------- | ---------- |
| 1      | 52  | 212 | 25  | 60  | 220               | 68.3       |
| 2      | 57  | 218 | 23  | 57  | 300               | 69.5       |
| 3      | 51  | 201 | 26  | 54  | 245               | 71         |
| 4      | 56  | 223 | 21  | 55  | 190               | 71.2       |

"""

answer_4 = """
**variables de decision**

  M_i, N_i, P_i, Q_i con i = 1,2,3,4: Tiempo asignado al equipo i para realizar las tareas M,N,P,Q del sistema

**restricciones**

Limitación de las horas de trabajo disponibles por cada equipo
  M_1 + N_1 + P_1 + Q_1 <= 220 
  M_2 + N_2 + P_2 + Q_2 <= 300 
  M_3 + N_3 + P_3 + Q_3 <= 245 
  M_4 + N_4 + P_4 + Q_4 <= 190 

Imposición de que terminen las 4 tareas que pueden ser parcialmente por cada uno de los equipos
  M_1 / 52  + M_2 / 57  + M_3 / 51  + M_4 / 56  = 1 
  N_1 / 212 + N_2 / 218 + N_3 / 201 + N_4 / 223 = 1 
  P_1 / 25  + P_2 / 23  + P_3 / 26  + P_4 / 21  = 1 
  Q_1 / 60  + Q_2 / 57  + Q_3 / 54  + Q_4 / 55  = 1 

No negatividad de las variables de decisión: 
  M_i >= 0
  N_i >= 0
  P_i >= 0
  Q_i >= 0
  con i = 1,2,3,4

**funcion objetivo**

min z = 68.3 * S_1 + 69.5 * S_2 + 71 * S_3 + 71.2 * S_4 
  S_i = M_i + N_i + P_i + Q_i 
  con i = 1,2,3,4
"""



problem_5 = """ 


"""
