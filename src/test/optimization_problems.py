
test_1 = """ 
Un granjero tiene un terreno de 10 hectáreas donde puede sembrar trigo, maíz y soja. 

**Tabla de recursos:**

| Recurso               | Trigo  | Maíz  | Soja | Disponibilidad |
| --------------------- | ------ | ----- | ---- | -------------- |
| Mano de obra (horas)  |   5    |   3   |   2  |      40        |
| Agua (m³)             |  100   |   80  |   60 |     800        |
| Fertilizante (kg)     |   10   |    8  |   6  |      80        |
| Ganancia (€/hectárea) |  500   |  400  |  300 |                |

**Resolver:**

El granjero desea obtener la mayor ganancia posible al finalizar la cosecha. Determinar cuántas hectáreas de cada cultivo debe sembrar para maximizar sus beneficios.
"""

test_2 = """
Una consultora necesita completar cuatro proyectos (A, B, C, D) para diferentes clientes. La consultora cuenta con cinco consultores a su disposición, cada uno con diferentes habilidades y disponibilidad horaria.

| Consultor | A   | B   | C   | D   | Horas disponibles | Coste/hora |
| --------- | --- | --- | --- | --- | ----------------- | ---------- |
| 1         | 15  | 200 | 30  | 30  | 500               | 89.3       |
| 2         | 20  | 220 | 30  | 20  | 550               | 90.5       |
| 3         | 25  | 240 | 30  | 40  | 500               | 76.4       |
| 4         | 30  | 260 | 30  | 50  | 505               | 69.4       |
| 5         | 10  | 280 | 10  | 10  | 450               | 100        | 

**Objetivo:**

La consultora desea determinar la asignación óptima de proyectos a los consultores, minimizando el costo total de la mano de obra, y asegurando que se cumplan los siguientes requisitos:

- **Completar todos los proyectos:** Cada proyecto debe ser completado en su totalidad.
- **Respetar la disponibilidad de los consultores:** Ningún consultor puede trabajar más horas de las que tiene disponibles.

**Pregunta:**

¿Cuántas horas debería dedicar cada consultor a cada proyecto para minimizar el costo total para la consultora, cumpliendo con los requisitos mencionados?

"""
