Algoritmo Minimax con Visualización de Árbol de Juego

Este programa implementa el algoritmo Minimax para la toma de decisiones en juegos de dos jugadores (MAX y MIN). Además de calcular el valor óptimo y el camino de decisión, genera una visualización gráfica del árbol de juego utilizando matplotlib.

Características
Construcción de un árbol de juego con nodos MAX, MIN y hojas terminales.

Implementación del algoritmo Minimax recursivo.

Visualización del árbol con:

Colores para cada tipo de nodo.

Camino óptimo resaltado.

Resumen de valores.

Explicaciones en consola del proceso paso a paso.

Requisitos
Antes de ejecutar el programa, instala las librerías necesarias:

pip install matplotlib numpy

Ejecución
Ejecuta el archivo en la terminal o desde un IDE:

python arboldejuego.py

El programa mostrará en consola:

La estructura del árbol.

Evaluación paso a paso de los nodos.

El valor óptimo para el jugador MAX y el camino recomendado.

Una visualización gráfica con el árbol y la tabla de valores.

Estructura del árbol utilizada
Nodo raíz: A (MAX)

Hijos: B (MIN), C (MIN), D (MIN)

Cada nodo MIN tiene tres hojas terminales con valores predefinidos.

Salida esperada
En consola:

Valor óptimo para MAX: 3
Camino óptimo: A → B → Hoja1
En ventana gráfica:

Visualización del árbol de juego con los valores calculados y el camino óptimo resaltado.
