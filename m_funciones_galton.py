#Módulo de funciones para simulación de modelo de Galton.
#Con 12 niveles y 3000 canicas. 

from importlib.metadata import distribution
import matplotlib.pyplot as plt
#Se importa matplotlib para la graficación del histograma.

def simular_galton(num_niveles=12, num_canicas=3000):
    """Simula el modelo de Galton.
    Parámetros:
    num_niveles (int): Número de niveles en la máquina de Galton (12).
    num_canicas (int): Número de canicas a simular (3000).
    
    Retorna:
    lista_posiciones (list): Lista con las posiciones finales de las canicas.
    """
    import random # Importa el módulo random para la simulación de movimientos aleatorios de las canicas al caer.
    
    lista_posiciones = []
    
    for _ in range(num_canicas):
        posicion = 0
        for _ in range(num_niveles):
            movimiento = random.choice([-1, 1])  # -1 para izquierda, 1 para derecha
            posicion += movimiento
        lista_posiciones.append(posicion)
    
    return lista_posiciones

def graficar_resultados(lista_posiciones):
    """Grafica los resultados de la simulación del modelo de Galton.
    Parámetros:
    lista_posiciones (list): Lista con las posiciones finales de las canicas.
    """
    plt.hist(lista_posiciones, bins=range(min(lista_posiciones), max(lista_posiciones) + 1), edgecolor='black')
    plt.title('Simulación del modelo de Galton')
    plt.xlabel('Distribución de canicas')
    plt.ylabel('Cantidad de canicas')
    plt.grid(True)
    plt.show()
    # Especificaciones del histograma: título, etiquetas y cuadrícula.