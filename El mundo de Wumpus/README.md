Mundo de Wumpus - Agente basado en percepciones
Descripción
Este proyecto implementa el clásico juego "Mundo de Wumpus" utilizando Prolog (SWI-Prolog) con una interfaz gráfica. El juego simula un agente que explora una cueva de 4x4 casillas, buscando oro mientras evita peligros como pozos y el temido Wumpus.

Características principales
Generación aleatoria del mundo: Wumpus, oro y pozos se colocan aleatoriamente al inicio.

Interfaz gráfica: Visualización del mundo en una matriz 4x4 con colores y símbolos.

Percepciones del agente: Brisa (pozos adyacentes), hedor (Wumpus adyacente), brillo (oro en la casilla).

Acciones disponibles: Moverse, girar, disparar flecha, recoger oro, salir de la cueva.

Lógica de decisión: El agente toma decisiones basadas en sus percepciones.

Requisitos
SWI-Prolog (con librería pce para la interfaz gráfica)

Instrucciones de uso
Cargar el archivo mundo_wunpus.pl en SWI-Prolog.

Ejecutar jugar. para iniciar el juego con interfaz gráfica.

Usar los botones en la interfaz o los comandos en la consola para interactuar.

Comandos principales:
jugar. - Inicia el juego con interfaz gráfica

siguiente_paso. - Ejecuta un paso automático del agente

reiniciar_juego. - Reinicia el mundo

mover_adelante. - Mueve el agente adelante

girar_izquierda. - Gira el agente a la izquierda

girar_derecha. - Gira el agente a la derecha

disparar_flecha. - Dispara una flecha

recoger_oro. - Recoge el oro si está presente

salir_cueva. - Sale de la cueva desde (1,1)

mostrar_info_completa. - Muestra información detallada del estado del juego

Mecánicas del juego

El agente comienza en la casilla (1,1) mirando al norte.

Debes encontrar el oro y regresar a la entrada para ganar.

Los pozos y el Wumpus matan al agente si entra en sus casillas.

Puedes disparar una flecha para matar al Wumpus si percibes hedor.

Estructura del código
Inicialización: Configuración inicial del mundo y posiciones aleatorias.

Percepciones: Detección de brisa, hedor y brillo.

Movimiento: Lógica para moverse y girar.

Interfaz gráfica: Visualización del mundo y controles.

Lógica del agente: Toma de decisiones basada en percepciones.

Autor
Implementado en SWI-Prolog con matriz visual.
