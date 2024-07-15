
# PROBLEMA DE ASIGNACION DE TAREAS





problem_1 = """ 
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

answer_2 = """
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




