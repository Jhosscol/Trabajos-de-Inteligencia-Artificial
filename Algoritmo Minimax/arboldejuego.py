import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

class NodoArbol:
    def __init__(self, valor=None, hijos=None, es_terminal=False, nombre=""):
        self.valor = valor
        self.hijos = hijos if hijos else []
        self.es_terminal = es_terminal
        self.nombre = nombre
        self.valor_calculado = None  # Para almacenar el valor calculado por minimax
        self.x = 0  # Coordenada x para el gráfico
        self.y = 0  # Coordenada y para el gráfico
    
    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def minimax(nodo, es_turno_max, profundidad=0, camino=[]):
    # Mostrar el estado actual
    indent = "  " * profundidad
    jugador = "MAX" if es_turno_max else "MIN"
    print(f"{indent}Evaluando nodo {nodo.nombre} - Turno de {jugador}")
    
    # Caso base: nodo terminal
    if nodo.es_terminal:
        print(f"{indent}→ Nodo terminal con valor: {nodo.valor}")
        nodo.valor_calculado = nodo.valor
        return nodo.valor, [nodo.nombre]
    
    # Inicializar valores según el jugador
    if es_turno_max:
        mejor_valor = float('-inf')
        print(f"{indent}Inicializando MAX con -∞")
    else:
        mejor_valor = float('inf')
        print(f"{indent}Inicializando MIN con +∞")
    
    mejor_camino = []
    
    # Evaluar todos los hijos
    for i, hijo in enumerate(nodo.hijos):
        print(f"{indent}Explorando hijo {i+1}/{len(nodo.hijos)}: {hijo.nombre}")
        
        valor, subcamino = minimax(hijo, not es_turno_max, profundidad + 1)
        
        print(f"{indent}Hijo {hijo.nombre} retornó valor: {valor}")
        
        # Actualizar el mejor valor según el jugador
        if es_turno_max:
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_camino = [nodo.nombre] + subcamino
                print(f"{indent}MAX actualiza: nuevo mejor valor = {mejor_valor}")
        else:
            if valor < mejor_valor:
                mejor_valor = valor
                mejor_camino = [nodo.nombre] + subcamino
                print(f"{indent}MIN actualiza: nuevo mejor valor = {mejor_valor}")
    
    nodo.valor_calculado = mejor_valor
    print(f"{indent}Nodo {nodo.nombre} ({jugador}) retorna: {mejor_valor}")
    return mejor_valor, mejor_camino

def asignar_coordenadas(nodo, x=0, y=0, nivel=0, ancho_nivel=8):
    """Asigna coordenadas a cada nodo para la visualización"""
    nodo.x = x
    nodo.y = y
    
    if nodo.hijos:
        num_hijos = len(nodo.hijos)
        ancho_hijo = ancho_nivel / max(1, num_hijos - 1) if num_hijos > 1 else 0
        x_inicial = x - ancho_nivel / 2
        
        for i, hijo in enumerate(nodo.hijos):
            if num_hijos == 1:
                x_hijo = x
            else:
                x_hijo = x_inicial + i * ancho_hijo
            y_hijo = y - 1.5
            asignar_coordenadas(hijo, x_hijo, y_hijo, nivel + 1, ancho_nivel * 0.6)

def dibujar_arbol(nodo, ax, camino_optimo=None):
    """Dibuja el árbol completo con los valores calculados"""
    
    def dibujar_nodo_recursivo(nodo_actual, es_en_camino=False):
        # Determinar el color del nodo
        if nodo_actual.es_terminal:
            color = '#ffeb3b' if es_en_camino else '#fff9c4'  # Amarillo para hojas
        elif 'MAX' in nodo_actual.nombre:
            color = '#4caf50' if es_en_camino else '#c8e6c9'  # Verde para MAX
        else:  # MIN
            color = '#f44336' if es_en_camino else '#ffcdd2'  # Rojo para MIN
        
        # Dibujar el nodo
        circulo = plt.Circle((nodo_actual.x, nodo_actual.y), 0.3, 
                           color=color, ec='black', linewidth=2 if es_en_camino else 1)
        ax.add_patch(circulo)
        
        # Agregar texto del nombre
        ax.text(nodo_actual.x, nodo_actual.y + 0.1, nodo_actual.nombre.split('(')[0], 
                ha='center', va='center', fontweight='bold', fontsize=8)
        
        # Agregar valor calculado
        if nodo_actual.valor_calculado is not None:
            ax.text(nodo_actual.x, nodo_actual.y - 0.15, str(nodo_actual.valor_calculado), 
                    ha='center', va='center', fontweight='bold', fontsize=10, color='blue')
        
        # Dibujar conexiones con los hijos
        for hijo in nodo_actual.hijos:
            hijo_en_camino = camino_optimo and hijo.nombre in camino_optimo
            # Línea más gruesa si está en el camino óptimo
            linewidth = 3 if (es_en_camino and hijo_en_camino) else 1
            color_linea = 'blue' if (es_en_camino and hijo_en_camino) else 'black'
            
            ax.plot([nodo_actual.x, hijo.x], [nodo_actual.y, hijo.y], 
                   color=color_linea, linewidth=linewidth)
            
            dibujar_nodo_recursivo(hijo, hijo_en_camino)
    
    # Empezar desde la raíz
    raiz_en_camino = camino_optimo and nodo.nombre in camino_optimo
    dibujar_nodo_recursivo(nodo, raiz_en_camino)

def crear_visualizacion(arbol, camino_optimo, valor_optimo):
    """Crea la visualización completa del algoritmo Minimax"""
    
    # Configurar la figura con subplots
    fig = plt.figure(figsize=(15, 12))
    
    # Subplot 1: Árbol del juego
    ax1 = plt.subplot(2, 1, 1)
    ax1.set_xlim(-6, 6)
    ax1.set_ylim(-5, 1)
    ax1.set_aspect('equal')
    ax1.set_title('Árbol del Juego - Algoritmo Minimax', fontsize=16, fontweight='bold')
    
    # Asignar coordenadas y dibujar el árbol
    asignar_coordenadas(arbol)
    dibujar_arbol(arbol, ax1, camino_optimo)
    
    # Leyenda
    legend_elements = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#4caf50', 
                   markersize=10, label='Nodo MAX'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#f44336', 
                   markersize=10, label='Nodo MIN'),
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#ffeb3b', 
                   markersize=10, label='Nodo Terminal'),
        plt.Line2D([0], [0], color='blue', linewidth=3, label='Camino Óptimo')
    ]
    ax1.legend(handles=legend_elements, loc='upper right')
    ax1.axis('off')
    
    # Subplot 2: Tabla de resultados
    ax2 = plt.subplot(2, 1, 2)
    ax2.axis('off')
    
    # Crear tabla de resultados
    tabla_datos = [
        ['Nodo', 'Tipo', 'Hijos', 'Operación', 'Valor'],
        ['B', 'MIN', '[3, 12, 8]', 'min(3, 12, 8)', '3'],
        ['C', 'MIN', '[2, 4, 6]', 'min(2, 4, 6)', '2'],
        ['D', 'MIN', '[14, 5, 2]', 'min(14, 5, 2)', '2'],
        ['A', 'MAX', '[3, 2, 2]', 'max(3, 2, 2)', '3']
    ]
    
    tabla = ax2.table(cellText=tabla_datos[1:], colLabels=tabla_datos[0],
                     cellLoc='center', loc='center',
                     colWidths=[0.1, 0.1, 0.2, 0.3, 0.1])
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1, 2)
    
    # Colorear la tabla
    for i in range(len(tabla_datos)):
        for j in range(len(tabla_datos[0])):
            cell = tabla[i, j]
            if i == 0:  # Header
                cell.set_facecolor('#e0e0e0')
                cell.set_text_props(weight='bold')
            elif tabla_datos[i][1] == 'MIN':
                cell.set_facecolor('#ffcdd2')
            elif tabla_datos[i][1] == 'MAX':
                cell.set_facecolor('#c8e6c9')
    
    # Añadir información adicional
    info_text = f"""
RESULTADO DEL ALGORITMO MINIMAX:

• Valor óptimo para el jugador MAX: {valor_optimo}
• Camino óptimo: {' → '.join(camino_optimo)}
• Decisión: MAX debe elegir la rama hacia el nodo B

EXPLICACIÓN:
1. Los nodos terminales (hojas) tienen valores fijos
2. Los nodos MIN eligen el valor mínimo de sus hijos
3. Los nodos MAX eligen el valor máximo de sus hijos  
4. El algoritmo propaga los valores hacia arriba recursivamente
    """
    
    ax2.text(0.02, 0.25, info_text, transform=ax2.transAxes, fontsize=11,
             verticalalignment='top', bbox=dict(boxstyle="round,pad=0.5", 
             facecolor="lightblue", alpha=0.8))
    
    plt.tight_layout()
    return fig

def construir_arbol_figura():
    # Nodos terminales (hojas)
    hojas = [
        NodoArbol(valor=3, es_terminal=True, nombre="Hoja1"),
        NodoArbol(valor=12, es_terminal=True, nombre="Hoja2"),
        NodoArbol(valor=8, es_terminal=True, nombre="Hoja3"),
        NodoArbol(valor=2, es_terminal=True, nombre="Hoja4"),
        NodoArbol(valor=4, es_terminal=True, nombre="Hoja5"),
        NodoArbol(valor=6, es_terminal=True, nombre="Hoja6"),
        NodoArbol(valor=14, es_terminal=True, nombre="Hoja7"),
        NodoArbol(valor=5, es_terminal=True, nombre="Hoja8"),
        NodoArbol(valor=2, es_terminal=True, nombre="Hoja9")
    ]
    
    # Nodos MIN (nivel 2)
    nodo_b = NodoArbol(nombre="B(MIN)")
    nodo_b.hijos = [hojas[0], hojas[1], hojas[2]]  # 3, 12, 8
    
    nodo_c = NodoArbol(nombre="C(MIN)")
    nodo_c.hijos = [hojas[3], hojas[4], hojas[5]]  # 2, 4, 6
    
    nodo_d = NodoArbol(nombre="D(MIN)")
    nodo_d.hijos = [hojas[6], hojas[7], hojas[8]]  # 14, 5, 2
    
    # Nodo MAX (raíz)
    raiz = NodoArbol(nombre="A(MAX)")
    raiz.hijos = [nodo_b, nodo_c, nodo_d]
    
    return raiz

def mostrar_arbol(nodo, nivel=0):
    indent = "  " * nivel
    if nodo.es_terminal:
        print(f"{indent}{nodo.nombre}: {nodo.valor}")
    else:
        print(f"{indent}{nodo.nombre}")
        for hijo in nodo.hijos:
            mostrar_arbol(hijo, nivel + 1)

def main():
    print("=" * 60)
    print("ALGORITMO MINIMAX - ÁRBOL DE JUEGOS CON VISUALIZACIÓN")
    print("=" * 60)
    
    # Construir el árbol
    print("\n1. ESTRUCTURA DEL ÁRBOL:")
    print("-" * 30)
    arbol = construir_arbol_figura()
    mostrar_arbol(arbol)
    
    print("\n2. EJECUCIÓN DEL ALGORITMO MINIMAX:")
    print("-" * 40)
    
    # Ejecutar Minimax
    valor_optimo, camino_optimo = minimax(arbol, True)  # Empezamos con MAX
    
    print("\n3. RESULTADOS:")
    print("-" * 20)
    print(f"Valor óptimo para MAX: {valor_optimo}")
    print(f"Camino óptimo: {' → '.join(camino_optimo)}")
    
    print("\n4. EXPLICACIÓN:")
    print("-" * 20)
    print("• Los nodos MAX buscan maximizar el valor")
    print("• Los nodos MIN buscan minimizar el valor")
    print("• El algoritmo explora todo el árbol de forma recursiva")
    print("• Cada nodo toma la decisión óptima según su tipo")
    
    # Mostrar los valores calculados para cada nodo intermedio
    print("\n5. VALORES DE LOS NODOS INTERMEDIOS:")
    print("-" * 35)
    print("• Nodo B (MIN): min(3, 12, 8) = 3")
    print("• Nodo C (MIN): min(2, 4, 6) = 2")
    print("• Nodo D (MIN): min(14, 5, 2) = 2")
    print("• Nodo A (MAX): max(3, 2, 2) = 3")
    
    print(f"\n➤ Por tanto, MAX debe elegir la rama hacia B para obtener el valor óptimo de {valor_optimo}")
    
    # Crear y mostrar la visualización
    print("\n6. GENERANDO VISUALIZACIÓN...")
    print("-" * 30)
    fig = crear_visualizacion(arbol, camino_optimo, valor_optimo)
    plt.show()
    
    # Opcional: guardar la imagen
    # fig.savefig('minimax_tree.png', dpi=300, bbox_inches='tight')
    # print("Visualización guardada como 'minimax_tree.png'")

if __name__ == "__main__":
    main()