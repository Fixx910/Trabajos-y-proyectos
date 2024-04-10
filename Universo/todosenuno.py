import subprocess
import random

# while True:
#     # Ejecutar el programa C++ para generar el archivo de datos
#     cpp_program = 'D:/ProgramasTC/universo/universobueno/output/universo.exe'
#     subprocess.run([cpp_program], check=True)

#     # Ejecutar el script de Python para graficar los datos
#     python_script = 'D:/ProgramasTC/universo/universobueno/graficaruniverso.py'
#     subprocess.run(['python', python_script], check=True)
#     entrada=input("Desea continuar? (s/n): ")
    
#     if entrada.lower() != "s":
#         break

while True:
    #Preguntar si quiere elegir el programa o que se eliga aleatoriamente
    entrada = input("Desea elegir el programa a ejecutar? (s/n):")
    if entrada.lower() == "n":
        #Generar un numero aleatorio entre 1 y 3
        numprograma= random.randint(1,3)

    else:
        #Listar los programas
        print("1.- Universo")
        print("2.- Tablero")
        print("3.- Busca palabras")
        numprograma = int(input("Elija el programa a ejecutar: "))
    
    #Ejecutar el programa seleccionado
    if numprograma==1:
        # Ejecutar el programa C++ para generar el archivo de datos
        cpp_program = 'D:/ProgramasTC/universo/universobueno/output/universo.exe'
        subprocess.run([cpp_program], check=True)

        # Ejecutar el script de Python para graficar los datos
        python_script = 'D:/ProgramasTC/universo/universobueno/graficaruniverso.py'
        subprocess.run(['python', python_script], check=True)
    elif numprograma==2:
        # Ejecutar el programa del juego del tablero
        python_script = 'D:\ProgramasTC/chessboard/estetableroeselfinal.py'
        subprocess.run(['python', python_script], check=True)
        
    elif numprograma==3:
        # Ejecutar el script de Python del buscador de palabras
        python_script = 'D:\ProgramasTC/buscapalabras/buscapalabras.py'
        subprocess.run(['python', python_script], check=True)
    else:
        print("Opción no válida")
    
    entrada=input("Desea continuar? (s/n): ")
    if entrada.lower() != "s":
        break


