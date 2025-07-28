Pacman con Algoritmo Minimax Avanzado

Descripción

Este proyecto implementa el clásico juego Pacman con una IA que utiliza el algoritmo Minimax mejorado con poda alfa-beta y tablas de transposición para tomar decisiones óptimas. El juego incluye un sistema de fantasmas inteligentes y un Pacman controlado por IA que intenta maximizar su puntuación mientras evita colisiones.

Características principales
Algoritmo Minimax avanzado con optimizaciones:

Poda alfa-beta para mayor eficiencia

Tabla de transposición para evitar cálculos redundantes

Función de evaluación sofisticada

IA para fantasmas con diferentes comportamientos:

Modo persecución

Modo asustado (cuando Pacman come un power pellet)

Movimiento semi-aleatorio

Sistema de juego completo:

Pellets normales y power pellets

Modo poder temporal

Sistema de vidas y niveles

Interfaz gráfica detallada con:

Tablero de juego

Panel de información

Estadísticas en tiempo real

Efectos visuales

Requisitos
Python 3.x

Biblioteca Pygame (pip install pygame)

Instrucciones de uso
Ejecución del juego:
Instalar las dependencias: pip install pygame

Ejecutar el script: python pacman_minimax.py

Seguir las instrucciones en pantalla para configurar la profundidad del algoritmo y activar/desactivar la poda alfa-beta

Controles durante el juego:
ESPACIO: Pausar/Reanudar

R: Reiniciar partida

+/-: Aumentar/Disminuir velocidad

1-5: Cambiar profundidad de la IA (1-5)

T: Activar/Desactivar tabla de transposición

A: Activar/Desactivar poda alfa-beta

Estructura del código
Clases principales:
GameState: Maneja el estado del juego (laberinto, posiciones, puntuación)

AdvancedMinimaxAgent: Implementa el algoritmo Minimax con optimizaciones

SmartGhostAI: Controla el comportamiento de los fantasmas

PacmanGame: Clase principal que maneja la interfaz gráfica y el bucle del juego

Funciones clave:
minimax(): Implementación del algoritmo de decisión con poda alfa-beta

evaluate_state(): Función de evaluación que considera múltiples factores

get_ghost_move(): Lógica de movimiento para los fantasmas

draw_maze() y draw_characters(): Renderizado del juego

draw_info_panel(): Muestra estadísticas y controles

Personalización
El juego permite ajustar varios parámetros:

Profundidad del algoritmo Minimax (1-6)

Activar/desactivar poda alfa-beta

Activar/desactivar tabla de transposición

Velocidad del juego

Estrategias implementadas
Para Pacman:

Prioriza comer pellets y power pellets

Evita fantasmas (excepto en modo poder)

Considera distancias a objetivos y amenazas

Penaliza movimientos repetitivos

Para fantasmas:

70% de movimientos inteligentes (persecución o huida)

30% de movimientos aleatorios

Comportamiento diferente en modo asustado

Estadísticas mostradas
Puntuación actual

Vidas restantes

Nivel

Pellets restantes

Nodos evaluados por la IA

Podas alfa-beta realizadas

Tiempo de cálculo

Estados en tabla de transposición

Historial de partidas

Notas
La IA de Pacman es configurable en cuanto a profundidad de búsqueda

El juego incluye efectos visuales como parpadeo para power pellets y fantasmas asustados

El panel lateral muestra información detallada sobre el estado del juego y la IA
