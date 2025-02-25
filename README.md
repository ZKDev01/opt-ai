# Optimization Bot

## Descripción del Proyecto. Objetivos y Limitaciones

Un modelo de optimización matemática es una herramienta fundamental en la toma de decisiones, compuesta por una función objetivo y un conjunto de restricciones en forma de sistemas de ecuaciones o inecuaciones. 

Este proyecto combina la potencia de los LLMs con la capacidad de análisis de documentos para crear un sistema que da respuestas a problemas de optimización matemática. Este sistema tiene las siguientes características:

1. *Análisis automático de problemas de optimización:* Capacidad de identificar el tipo de problema de optimización al analizar las entradas del usuario y posibilidad de analizar información proporcionada por el usuario, como tablas, para determinar si corresponde a un problema de optimización matemática  
2. *Generación de soluciones óptimas:* Uso de LLMs para analizar grandes cantidades de información y generar soluciones óptimas para problemas de optimización complejos
3. *Análisis de documentos:* Capacidad de analizar documentos relevantes para proporcionar contexto adicional a la respuesta que proporcione al usuario 
4. *Uso de técnicas de Ingeniería de Prompt:* Aplicación de ToT (Tree-of-Thought) y CoT (Chain-of-Thought) para mejorar la precisión de las respuestas 

Este sistema enfrenta algunas limitaciones importantes:

1. *Precisión potencialmente baja:* La respuesta proporcionada por el sistema no garantiza siempre la correctitud matemática
2. *Complejidad temporal:* El uso de técnicas de Ingeniería de Prompt, junto con cada llamada al LLM, puede aumentar significativamente el tiempo necesario para procesar y responder a las consultas

## Instalación del Proyecto

