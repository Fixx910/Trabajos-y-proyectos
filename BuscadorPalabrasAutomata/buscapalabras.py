import graphviz

estados={
    1:{'f':[1], 'e':[2],'t':[9],'v':[17]},
    2:{'f':[1], 'm':[3],'t':[9],'v':[17]},
    3:{'f':[1], 'i':[4],'t':[9],'v':[17]},
    4:{'f':[1], 'n':[5],'t':[9],'v':[17]},
    5:{'f':[1], 'i':[22],'a':[6],'t':[9],'v':[17]},
    6:{'f':[1], 'z':[7],'t':[9],'v':[17]},
    7:{'f':[1], 'i':[8],'t':[9],'v':[17]},
    8:{'f':[1], 't':[9],'v':[17]},
    9:{'f':[1], 'o':[10],'t':[9],'v':[17]},
    10:{'f':[1], 'n':[11],'r':[14],'t':[9],'v':[17]},
    11:{'f':[1], 't':[12],'v':[17]},
    12:{'f':[1], 'a':[13],'t':[9],'v':[17]},
    13:{'f':[1],'t':[9],'v':[17]},
    14:{'f':[1], 't':[25],'v':[17]},
    15:{'f':[1], 'a':[16],'t':[9],'v':[17]},
    16:{'f':[1],'t':[9],'v':[17]},
    17:{'f':[1], 'i':[18],'t':[9],'v':[17]},
    18:{'f':[1], 'e':[19],'t':[9],'v':[17]},
    19:{'f':[1], 'j':[20],'t':[9],'v':[17]},
    20:{'f':[1], 'a':[21],'t':[9],'v':[17]},
    21:{'f':[1], 't':[9],'v':[17]},
    22:{'f':[1], 's':[23],'t':[9],'v':[17]},
    23:{'f':[1], 't':[26],'v':[17]},
    24:{'f':[1],'t':[9],'v':[17]},
    25:{'a':[16],'o':[10]},
    26:{'o':[10],'a':[16]}
}
def leer_documento(archivo):
    with open(archivo, 'r') as file:
        texto = file.read()
    return texto

import string

def encontrar_posiciones(texto, estados, estado_inicial):
    estado_actual = [estado_inicial]  # Cambiar el estado actual a una lista de estados
    parrafo = 1
    palabra = 1
    posiciones = []

    palabra_actual = ""
    for caracter in texto:
        if caracter.isspace() or caracter in string.punctuation:
            for estado in estado_actual:  # Iterar sobre todos los estados actuales
                if estado in estados:
                    if 't' in estados[estado]:  # Verificar si estamos en un estado de aceptación
                        posiciones.append((parrafo, palabra, palabra_actual))
            estado_actual = [estado_inicial]
            palabra += 1
            palabra_actual = ""
            if caracter == '\n':
                parrafo += 1
                palabra = 1
        else:
            nuevos_estados = []
            for estado in estado_actual:  # Iterar sobre todos los estados actuales
                if estado in estados and caracter in estados[estado]:
                    nuevos_estados.extend(estados[estado][caracter])
            estado_actual = nuevos_estados
            palabra_actual += caracter

    return posiciones




def graficar_dfa(estados, estado_inicial, posiciones_coincidencia):
    dot = graphviz.Digraph()

    # Agregar estados y transiciones al gráfico
    for estado, transiciones in estados.items():
        if estado in posiciones_coincidencia:
            dot.node(str(estado), label=str(estado), color='red', style='filled')
        elif estado == estado_inicial:
            dot.node(str(estado), label=str(estado), shape='doublecircle')
        else:
            dot.node(str(estado), label=str(estado))

        for entrada, destino in transiciones.items():
            for estado_destino in destino:
                dot.edge(str(estado), str(estado_destino), label=entrada)

    # Renderizar y mostrar el gráfico
    dot.render('dfa', format='png', view=True)


# Leer el archivo
texto = leer_documento("D:/ProgramasTC/buscapalabras/documento.txt")

# Definir el estado inicial del autómata
estado_inicial = 1

# Encontrar las posiciones donde se encuentran las coincidencias con el autómata
posiciones_coincidencia = encontrar_posiciones(texto, estados, estado_inicial)

# Imprimir las posiciones encontradas
for parrafo, palabra, palabra_encontrada in posiciones_coincidencia:
    print(f"Coincidencia encontrada en el párrafo {parrafo}, palabra {palabra}: {palabra_encontrada}.")

# Llamada a la función para graficar el DFA
graficar_dfa(estados, estado_inicial, posiciones_coincidencia)
