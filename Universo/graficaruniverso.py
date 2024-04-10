import matplotlib.pyplot as plt
import numpy as np

# Función para contar el número de 'a' en una cadena
def contar_a(cadena):
    return cadena.count('a')

# Leer el archivo de salida
with open('D:\ProgramasTC/universo/universobueno/output/Universo.txt', 'r') as archivo:
    contenido = archivo.read()

# Extraer las combinaciones de bits del contenido del archivo
combinaciones = contenido.split('{')[1].split('}')[0].split(',')

# Calcular el número de 'a' para cada cadena
numeros_a = [contar_a(cadena) for cadena in combinaciones]

# Crear lista de etiquetas para el eje x
etiquetas_x = range(len(combinaciones))

# Graficar
fig, axs = plt.subplots(2, figsize=(10, 6))

# Gráfico lineal
axs[0].plot(etiquetas_x, numeros_a, marker='o', linestyle='-', color='b')
axs[0].set_xlabel('Cadenas')
axs[0].set_ylabel('Número de \'a\'')
axs[0].set_title('Número de \'a\' en cada cadena (Escala Lineal)')
axs[0].grid(True)

# Gráfico con escala logarítmica en ambos ejes
axs[1].plot(etiquetas_x, numeros_a, marker='o', linestyle='-', color='b')
axs[1].set_xlabel('Cadenas (log)')
axs[1].set_ylabel('Número de \'a\' (log)')
axs[1].set_title('Número de \'a\' en cada cadena (Escala Logarítmica)')
axs[1].set_yscale('log')
axs[1].set_xscale('log')
axs[1].grid(True)

# Ajuste de la ventana a pantalla completa
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

plt.show()
