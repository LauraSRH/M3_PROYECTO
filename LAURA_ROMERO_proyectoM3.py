#Modelo de Galton, para 12 niveles y 3000 canicas, que no tenga distribución normal, 
#sino una distribución diferente.
# 1. Simulación de una máquina de Galton de 3000 canicas.
# 2. 12 niveles de obstáculos -se debera decidir si va a caer a un lado o al otro 12 veces.
# 3. El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, 
# 4. Emplear dos funciones, una para calcular los resultados de las canicas y 
# la segunda para la graficación del histograma.

from m_funciones_galton import simular_galton, graficar_resultados # Importa las funciones del módulo para la simulación
import matplotlib.pyplot as plt
# Definición de los parámetros
num_niveles = 12
num_canicas = 3000
# Simulación
posiciones_finales = simular_galton(num_niveles, num_canicas) #  la caida de las canicas, izq/der con 
# -1 y +1 respectivamente para los doce niveles
# Graficación
graficar_resultados(posiciones_finales)

print("Simulación completada y gráfico generado.")

