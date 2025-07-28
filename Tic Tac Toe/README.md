Tres en Raya con Algoritmo Minimax

Descripción

Este proyecto implementa el clásico juego Tres en Raya (Tic-Tac-Toe) con una IA invencible que utiliza el algoritmo Minimax para tomar decisiones óptimas. El programa ofrece dos modos de juego: por consola y con interfaz gráfica.

Características principales

- Algoritmo Minimax: IA invencible que evalúa todos los posibles movimientos.

Dos modos de juego:

- Interfaz gráfica con TKinter

- Versión por consola

- Sistema de puntuación: Lleva registro de victorias, derrotas y empates.

- Interfaz intuitiva: Diseño moderno con colores atractivos.

Requisitos:

- Python 3.x

- Biblioteca TKinter (normalmente incluida en Python estándar)

Instrucciones de uso

Para la versión gráfica:

- Ejecutar el script: python Minimax_tictactoe.py

- Seleccionar la opción 2 (Interfaz gráfica) o simplemente ejecutará esta opción por defecto.

- Jugar haciendo clic en los cuadros del tablero.

- Usar los botones "Nuevo Juego" y "Reiniciar Marcador" según sea necesario.

Para la versión por consola:

- Ejecutar el script: python Minimax_tictactoe.py

- Seleccionar la opción 1 (Consola).

- Introducir números del 0 al 8 para indicar tu movimiento (las posiciones se muestran en el tablero de referencia).

Estructura del código

Clases principales:

- TicTacToeGame: Lógica principal del juego

- Maneja el tablero y las reglas

- Implementa el algoritmo Minimax

- Proporciona versión por consola

- TicTacToeGUI: Interfaz gráfica

- Tablero interactivo con botones

- Sistema de puntuación

- Diseño visual con colores temáticos

Funciones clave:

- minimax(): Implementación del algoritmo de decisión

- get_best_move(): Determina el mejor movimiento para la IA

- is_winner(): Verifica condiciones de victoria

- player_move() y ai_move(): Manejan los turnos del juego

Personalización

Puedes modificar:

- Los colores en la clase TicTacToeGUI

- El delay de la IA (actualmente 500ms)

- Los valores de puntuación en el algoritmo Minimax

Notas

La IA es perfecta (no se puede ganar, solo empatar con juego óptimo)

El diseño está optimizado para una ventana de 400x500 píxeles

Autor

Implementado en Python con TKinter y algoritmo Minimax.
