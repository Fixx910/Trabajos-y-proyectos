import pygame
import numpy as np
import random
import time
import csv 
import networkx as nx
import matplotlib.pyplot as plt



# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

# Cargar la imagen del tablero
tablero_image = pygame.image.load('D:/ProgramasTC/chessboard/tablero.png')
pygame.display.set_caption("Botón de Inicio")


# Definir los colores de las casillas
colors = ['black', 'red']
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Crear un botón
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Iniciar Animación", True, BLACK)
button_rect = button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

states = {
    1: {'B': [6], 'R': [2, 5]},
    2: {'B': [1, 3, 6], 'R': [5, 7]},
    3: {'B': [6, 8], 'R': [2, 4, 7]},
    4: {'B': [3, 8], 'R': [7]},
    5: {'B': [1, 6, 9], 'R': [2, 10]},
    6: {'B': [1, 3, 9, 11], 'R': [2, 5, 7, 10]},
    7: {'B': [3, 6, 8, 11], 'R': [2, 4, 10, 12]},
    8: {'B': [3, 11], 'R': [4, 7, 12]},
    9: {'B': [6, 14], 'R': [5, 10, 13]},
    10: {'B': [6, 9, 11, 14], 'R': [5, 7, 13, 15]},
    11: {'B': [6, 8, 14, 16], 'R': [7, 10, 12, 15]},
    12: {'B': [8, 11, 16], 'R': [7, 15]},
    13: {'B': [9, 14], 'R': [10]},
    14: {'B': [9, 11], 'R': [10, 13, 15]},
    15: {'B': [11, 14, 16], 'R': [10, 12]},
    16: {'B': [11], 'R': [12, 15]}
}



def find_all_paths(states, start_state, moves):
    paths = []

    def find_paths(current_state, remaining_moves, path=[]):
        path.append(current_state)

        if len(remaining_moves) == 0:
            paths.append(path[:])
        else:
            next_color = remaining_moves[0]
            next_states = states[current_state][next_color]

            for next_state in next_states:
                find_paths(next_state, remaining_moves[1:], path)

        path.pop()

    find_paths(start_state, moves)
    return paths

def find_valid_pathsP1(states, start_state, moves):
    valid_paths = []

    def find_paths(current_state, remaining_moves, path=[]):
        path.append(current_state)

        if len(remaining_moves) == 0:
            if current_state == 16:
                valid_paths.append(path[:])
        else:
            next_color = remaining_moves[0]
            next_states = states[current_state][next_color]

            for next_state in next_states:
                find_paths(next_state, remaining_moves[1:], path)

        path.pop()

    find_paths(start_state, moves)
    return valid_paths


def find_valid_pathsP2(states, start_state, moves):
    valid_paths = []

    def find_paths(current_state, remaining_moves, path=[]):
        path.append(current_state)

        if len(remaining_moves) == 0:
            if current_state == 13:
                valid_paths.append(path[:])
        else:
            next_color = remaining_moves[0]
            next_states = states[current_state][next_color]

            for next_state in next_states:
                find_paths(next_state, remaining_moves[1:], path)

        path.pop()

    find_paths(start_state, moves)
    return valid_paths

def save_paths_to_csv(paths, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        for path in paths:
            csv_writer.writerow([','.join(map(str, path))])

def load_paths_from_csv(filename):
    paths = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            path = list(map(int, row[0].split(',')))
            paths.append(path)
    return paths

# Función para mostrar los jugadores en el tablero
def show_players(player_positions):
    screen.fill((0, 0, 0))  # Rellenar la pantalla con negro
    screen.blit(tablero_image, (0, 0))  # Dibujar el tablero en la pantalla
    for i in range(4):
        for j in range(4):
            index = i * 4 + j + 1
            if index in player_positions[0]:
                screen.blit(player1_image, (j * 100, i * 100))  # Dibujar la imagen del jugador 1
            if index in player_positions[1]:
                screen.blit(player2_image, (j * 100, i * 100))  # Dibujar la imagen del jugador 2
    pygame.display.flip()  # Actualizar la pantalla


def actualizar_rutas_validas(archivo_rutas_P1, archivo_rutas_P2):
    rutas_validas_P1 = []
    rutas_validas_P2 = []

    # Cargar rutas válidas desde el archivo CSV correspondiente para el jugador 1
    with open(archivo_rutas_P1, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            ruta = list(map(int, row[0].split(',')))
            rutas_validas_P1.append(ruta)

    # Cargar rutas válidas desde el archivo CSV correspondiente para el jugador 2
    with open(archivo_rutas_P2, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            ruta = list(map(int, row[0].split(',')))
            rutas_validas_P2.append(ruta)

    # Verificar las rutas válidas según las condiciones especificadas
    rutas_validas = []
    for ruta_P1 in rutas_validas_P1:
        for ruta_P2 in rutas_validas_P2:
            overlapping = False
            for i in range(min(len(ruta_P1), len(ruta_P2))):
                if ruta_P1[i] == ruta_P2[i]:
                    overlapping = True
                    break

            if not overlapping:
                rutas_validas.append((ruta_P1, ruta_P2))

def actualizar_rutas_validas2(ruta_seleccionadaP1, archivo_rutas_P2,starting_player):
    #actualizar rutas validas para el jugador 2
    ruta_P1 = load_paths_from_csv(ruta_seleccionadaP1)[0]
    rutas_validas_P2 = []

    with open(archivo_rutas_P2, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            ruta = list(map(int, row[0].split(',')))
            rutas_validas_P2.append(ruta)

    
    # Verificar las rutas válidas según las condiciones especificadas
    rutas_validas = []
    for ruta_P2 in rutas_validas_P2:
        overlapping = False
        for i in range(min(len(ruta_P1), len(ruta_P2))):
            if ruta_P1[i] == ruta_P2[i]:
                overlapping = True
                break
        if starting_player==1:
            if len(ruta_P1) == len(ruta_P2):
                for i in range(0,min(len(ruta_P1), len(ruta_P2))-1):
                    if ruta_P1[i+1] == ruta_P2[i]:
                        overlapping = True
                        break
            else:
                for i in range(0,min(len(ruta_P1), len(ruta_P2))-1):
                    if ruta_P1[i+1] == ruta_P2[i]:
                        overlapping = True
                        break
        else:
            for i in range(0,min(len(ruta_P1), len(ruta_P2))-1):
                if ruta_P2[i+1] == ruta_P1[i]:
                    overlapping = True
                    break

        if not overlapping:
            rutas_validas.append((ruta_P2))


    with open("Nuevas_RutasP2.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows([','.join(map(str, ruta_P2))] for ruta_P2 in rutas_validas)

def graficar_nfa(states, moves):
    # Crear un gráfico dirigido
    G = nx.DiGraph()

    # Agregar nodos al gráfico
    for state in states.keys():
        G.add_node(state)

    # Agregar arcos ponderados al gráfico
    for state, transitions in states.items():
        for move, next_states in transitions.items():
            for next_state in next_states:
                G.add_edge(state, next_state, label=move)

    # Crear un gráfico de posiciones para mejorar la visualización
    pos = nx.spring_layout(G)

    # Dibujar nodos y arcos con etiquetas
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')
    edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar el gráfico
    plt.axis('off')
    plt.show()

#Bucle para decidir si jugar en automatico o en manual
while True:
    #Elegir 
    modo_juego = input("Quieres jugar de manera automatica (A) o manual (M)? ").upper()

    if modo_juego=='A':
        min_movs=4
        max_movs=10
        long_mov=random.randint(min_movs, max_movs)
        moves = [random.choice(['R', 'B']) for _ in range(long_mov)]  # Generar secuencia aleatoria para el jugador 1
        moves = [move.strip() for move in moves]
        moves2 = [random.choice(['R', 'B']) for _ in range(long_mov)]  # Generar secuencia aleatoria para el jugador 2
        moves2 = [move2.strip() for move2 in moves2]

        print("Secuencia de movimientos para el jugador 1:", moves)
        print("Secuencia de movimientos para el jugador 2:", moves2)
    elif modo_juego=='M':
        moves = input("Ingrese la secuencia de movimientos (separe cada movimiento por coma): ").upper().split(',')
        moves=['B','B','B','R','B']
        # moves = [move.strip() for move in moves]

        moves2 = input("Ingrese la secuencia de movimientos (separe cada movimiento por coma): ").upper().split(',')
        moves2=['R','B','R','B','R']
        # moves2 = [move2.strip() for move2 in moves2]
    else:
        print("Opcion no valida")
        continue

    start_state_P1 = 1
    start_state_P2 = 4

    #Vemos quien inicia turno
    starting_player = random.choice([1, 2])
    print("El jugador", starting_player, "inicia el juego.")

    ##RUTAS PARA JUGADOR 1 Y JUGADOR 2
    all_pathsP1 = find_all_paths(states, start_state_P1, moves)
    save_paths_to_csv(all_pathsP1, "Todas_RutasP1.csv")
    all_pathsP2 = find_all_paths(states, start_state_P2, moves2)
    save_paths_to_csv(all_pathsP2, "Todas_RutasP2.csv")

    #Rutas validas para jugador 1 y jugador 2
    valid_pathsP1 = find_valid_pathsP1(states, start_state_P1, moves)
    save_paths_to_csv(valid_pathsP1, "Rutas_ValidasP1.csv")
    valid_pathsP2 = find_valid_pathsP2(states, start_state_P2, moves2)
    save_paths_to_csv(valid_pathsP2, "Rutas_ValidasP2.csv")

    print("\nTodas las rutas guardadas en 'Todas_Rutas.csv'")
    print("Rutas válidas guardadas en 'Rutas_Validas.csv'")

    # Bucle para verificar la existencia de rutas válidas para jugardor 1
    while True:
        # Verificar si hay rutas válidas para el jugador 1
        if not valid_pathsP1:
            print("No existe ruta válida para el jugador 1.")
            if modo_juego == 'A':
                print("¿Quieres probar otra secuencia de movimientos para el jugador 1? (Sí/No):  ")
                retry = 's'
            else:
                retry = input("¿Quieres probar otra secuencia de movimientos para el jugador 1? (Sí/No): ").strip().lower()
            if retry in ['sí', 'si', 's']:
                if modo_juego == 'A':
                    long_mov = random.randint(min_movs, max_movs)
                    moves = [random.choice(['R', 'B']) for _ in range(long_mov)]
                    valid_pathsP1 = find_valid_pathsP1(states, start_state_P1, moves)
                    save_paths_to_csv(valid_pathsP1, "Rutas_ValidasP1.csv")
                    print("Secuencia de movimientos para el jugador 1:", moves)
                else:
                    moves = input("Ingrese la secuencia de movimientos para el jugador 1: ").upper().split(',')
                    moves = [move.strip() for move in moves]
                    valid_pathsP1 = find_valid_pathsP1(states, start_state_P1, moves)
                    save_paths_to_csv(valid_pathsP1, "Rutas_ValidasP1.csv")
            else:
                exit()
        else:
            break
    contadorrutasvalidasp1=0
    #Actualizamos las rutas 
    # actualizar_rutas_validas("Rutas_ValidasP1.csv", "Rutas_ValidasP2.csv")
    # print("Se han actualizado los archivos CSV de rutas válidas.")
    
    #imprimir rutas validas para p1
    print("\nRutas válidas para el jugador 1:")
    for i, path in enumerate(valid_pathsP1, 1):
        print(f"Ruta {i}: {path}")
        contadorrutasvalidasp1+=1
    
    print("Selecciona una ruta para el jugador 1.")

    if modo_juego == 'A':
        #Elige una ruta aleatoria
        selected_path_index_P1 = random.randint(0,contadorrutasvalidasp1-1)
    else:
        selected_path_index_P1 = int(input("\nElige una ruta para el jugador 1 (ingrese el número de ruta): ")) - 1


    selected_path_P1 = valid_pathsP1[selected_path_index_P1]
    #imprimimos la ruta seleccionada de p1
    print("\nRuta seleccionada para el jugador 1:", selected_path_P1)
    save_paths_to_csv([selected_path_P1], "Ruta_Seleccionada_P1.csv")

    # Verificar si hay rutas válidas para el jugador 2
    valid_pathsP2_verificados=[]
    actualizar_rutas_validas2("Ruta_Seleccionada_P1.csv","Rutas_ValidasP2.csv",starting_player)

    with open("Nuevas_RutasP2.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            ruta = list(map(int, row[0].split(',')))
            valid_pathsP2_verificados.append(ruta)


    # Bucle para verificar la existencia de rutas válidas para el jugador 2 (solo si la verificacion anterior no encuentra rutas validas)
    # Una vez elegido el camino para el jugador 1, se verifica si hay rutas válidas para el jugador 2
    # Si no hay rutas válidas, se le da la opción al usuario de probar otra secuencia de movimientos para el jugador 2
    # Para que una ruta sea valida tiene que cumplir con las condiciones:
    # 1. No debe haber turno en donde estén en el mismo estado
    # 2. Para el primer jugador el turno i+1 debe ser diferente al turno i del segundo jugador
    # 3. Deben llegar a la meta
    
    while True:
        # Verificar si hay rutas válidas para el jugador 2
        if not valid_pathsP2_verificados:
            print("No existe ruta válida para el jugador 2.")
            if modo_juego == 'A':
                print("¿Quieres probar otra secuencia de movimientos para el jugador 2? (Sí/No):  ")
                retry = 's'
            else:
                retry = input("¿Quieres probar otra secuencia de movimientos para el jugador 2? (Sí/No): ").strip().lower()
            if retry in ['sí', 'si', 's']:
                if modo_juego == 'A':
                    long_mov = random.randint(min_movs, max_movs)
                    moves2 = [random.choice(['R', 'B']) for _ in range(long_mov)]
                    print("Secuencia de movimientos para el jugador 2:", moves2)
                    valid_pathsP2 = find_valid_pathsP2(states, start_state_P2, moves2)
                    # Cargar rutas válidas desde el archivo CSV correspondiente para el jugador 2
                    save_paths_to_csv(valid_pathsP2, "Rutas_ValidasP2.csv")
                    actualizar_rutas_validas2("Ruta_Seleccionada_P1.csv","Rutas_ValidasP2.csv",starting_player)
                    
                    with open("Nuevas_RutasP2.csv", 'r') as csvfile:
                        csv_reader = csv.reader(csvfile)
                        for row in csv_reader:
                            ruta = list(map(int, row[0].split(',')))
                            valid_pathsP2_verificados.append(ruta)
                else:
                    moves2 = input("Ingrese la secuencia de movimientos para el jugador 2: ").upper().split(',')
                    moves2 = [move.strip() for move in moves2]
                    print("Secuencia de movimientos para el jugador 2:", moves2)
                    valid_pathsP2 = find_valid_pathsP2(states, start_state_P2, moves2)
                    save_paths_to_csv(valid_pathsP2, "Rutas_ValidasP2.csv")
                    actualizar_rutas_validas2("Ruta_Seleccionada_P1.csv","Rutas_ValidasP2.csv")
                    
                    with open("Nuevas_RutasP2.csv", 'r') as csvfile:
                        csv_reader = csv.reader(csvfile)
                        for row in csv_reader:
                            ruta = list(map(int, row[0].split(',')))
                            valid_pathsP2_verificados.append(ruta)
            else:
                exit()
        else:
            break
  
    #imprimir rutas validas para p2
    contadorrutasvalidasp2=0
    print("\nRutas válidas para el jugador 2:")
    for i, path in enumerate(valid_pathsP2_verificados, 1):
        print(f"Ruta {i}: {path}")
        contadorrutasvalidasp2+=1

    #Seleccionamos la ruta para el jugador 2
    if modo_juego == 'A':
        selected_path_index_P2 = random.randint(0,contadorrutasvalidasp2-1)
    else:
        selected_path_index_P2= int(input("Elige una ruta para el jugador 2 (ingrese el número de ruta): ")) - 1
    selected_path_P2 = valid_pathsP2_verificados[selected_path_index_P2]

    # Guardar las rutas seleccionadas en archivos CSV para cada jugador
    save_paths_to_csv([selected_path_P2], "Ruta_Seleccionada_P2.csv")
    print("\nLas rutas seleccionadas para cada jugador se han guardado en los archivos 'Ruta_Seleccionada_P1.csv' y 'Ruta_Seleccionada_P2.csv'.")

    # Imprimir las rutas seleccionadas
    print("\nRuta seleccionada para el jugador 1:", selected_path_P1)
    print("Ruta seleccionada para el jugador 2:", selected_path_P2)

    # Crear la pantalla
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Movimientos de Jugadores")

    # Rutas de ejemplo para los jugadores
    player1_path = selected_path_P1
    player2_path = selected_path_P2

    # Inicializar las posiciones de los jugadores

    # Cargar las imágenes de los jugadores
    player1_image = pygame.image.load('D:/ProgramasTC/chessboard/player1.png')
    player2_image = pygame.image.load('D:/ProgramasTC/chessboard/player2.png')
    player_positions = [[1], [4]]


    


    #Verificamos quien tiene la ruta mas larga
    if len(player1_path) > len(player2_path):
        print("El jugador 1 tiene la ruta más larga.")
        recorridofinal=200*len(player1_path)
    elif len(player1_path) < len(player2_path):
        print("El jugador 2 tiene la ruta más larga.")
        recorridofinal=200*len(player2_path)
    else:
        print("Ambos jugadores tienen rutas de la misma longitud.")
        recorridofinal=200*len(player1_path)

    print("El jugador inicial es el jugador", starting_player,)

    clock=pygame.time.Clock()
    
    
    # Bucle principal
    running = True
    animation_started = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar si se hizo clic en el botón
                if button_rect.collidepoint(event.pos):
                    animation_started = True

        # Dibujar la pantalla
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, button_rect, 2)
        screen.blit(button_text, button_rect.topleft)

        # Actualizar la pantalla
        show_players(player_positions)
        pygame.display.flip()
        clock.tick(1)
        if animation_started:
            # Realizar los movimientos alternados
            # Dependiendo de que jugador inicia se muestran los movimientos
            if starting_player == 1:
                for i in range(1, recorridofinal):
                    if i < len(player1_path):
                        player_positions[0] = [player1_path[i]]
                        show_players(player_positions)
                        pygame.display.flip()
                        print("Jugador 1 en casilla: ", player1_path[i])
                        pygame.time.wait(500)
                    if i < len(player2_path):
                        player_positions[1] = [player2_path[i]]
                        show_players(player_positions)
                        pygame.display.flip()
                        print("Jugador 2 en casilla: ", player2_path[i])
                        pygame.time.wait(500)
                break
            else:
                
                for i in range(1, recorridofinal):
                    if i < len(player2_path):
                        player_positions[1] = [player2_path[i]]
                        show_players(player_positions)
                        print("Jugador 2 en casilla: ", player2_path[i])
                        pygame.display.flip()
                        pygame.time.wait(500)
                    if i < len(player1_path):
                        player_positions[0] = [player1_path[i]]
                        show_players(player_positions)
                        print("Jugador 1 en casilla: ", player1_path[i])
                        pygame.display.flip()
                        pygame.time.wait(500)
                break
        pygame.time.wait(500)
        
        
    # Salir de pygame
    pygame.quit()

    # Graficar el NFA
    graficar_nfa(states, moves)
    graficar_nfa(states, moves2)
    

    # Preguntar si quiere jugar otra vez
    jugarotravez=input("Quieres jugar otra vez? (s/n)").upper()
    if jugarotravez=='S':
        continue
    else:
        break


