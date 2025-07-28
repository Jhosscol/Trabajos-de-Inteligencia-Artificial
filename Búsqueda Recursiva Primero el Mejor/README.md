Búsqueda Recursiva Mejor-Primero (RBFS) en Mapa de Rumanía

Este programa implementa el algoritmo RBFS (Recursive Best-First Search) para encontrar el camino más económico entre dos ciudades del mapa de Rumanía. El problema se resuelve utilizando un grafo con distancias y una heurística basada en la distancia estimada a la ciudad objetivo (Bucarest).

Características
Representación del mapa de Rumanía como un grafo con distancias reales entre ciudades.

Implementación de la búsqueda RBFS, que usa:

Costo acumulado g(n).

Heurística h(n) (distancia estimada).

Evaluación f(n) = max(g+h, f_padre).

Reconstrucción y visualización del camino óptimo en consola.

Salida con el costo total del recorrido.

Requisitos
Antes de ejecutar el programa, asegúrate de tener Python 3 instalado. Este script no requiere librerías externas.

Ejecución
Ejecuta el programa directamente en la terminal:

python brpm.py
Funcionamiento del algoritmo
Estado inicial: Ciudad Arad.

Objetivo: Llegar a Bucarest.

Expansión: Se exploran ciudades vecinas en orden de menor f(n).

Búsqueda recursiva: Se ajusta el límite f dinámicamente para minimizar memoria.

Resultado: Camino óptimo y costo total.

Salida esperada
En consola se mostrará algo como:

Camino encontrado: Arad → Sibiu → Fagaras → Bucarest
Costo total: 450
(El camino y el costo pueden variar según el grafo y heurística utilizada).

Autor
Trabajo realizado como parte del curso de Inteligencia Artificial y Algoritmos de Búsqueda.
