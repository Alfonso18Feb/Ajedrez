from ajedrez import *
from piezas import *
def iniciar_partida(nombre_fichero):
    # Representamos un tablero como una cadena separando las filas por cambios de línea y las columnas por tabuladores.
    tablero_inicial = [["♜","♞","♝","♛","♚","♝","♞","♜"],
                       ["♟","♟","♟","♟","♟","♟","♟","♟"],
                       [" "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "],
                       [" "," "," "," "," "," "," "," "],
                       ["♙","♙","♙","♙","♙","♙","♙","♙"],
                       ["♖","♘","♗","♕","♔","♗","♘","♖"]]

    f = open(nombre_fichero, 'w', encoding="utf8")
    #abre la tabla(nombre_fichero) en formato escritura(w=writting) y aceptando los caracteres UniCode (utf8) 
    for i in range(8):
        for j in range(8):
            f.write(tablero_inicial[i][j]+"\t")
            # separa cada columna con un tabulado
        f.write("\n")
        #separa cada fila con un salto de linea
    f.close()
    #cierra la tabla
    movimiento = 0
    # Bucle condicional para realizar movimientos en la partida hasta que el usario decida terminar.
    while True:
        Ajedrez.imprimir_tablero(nombre_fichero, movimiento)
        #imprime el tablero despues de cada movimiento para decidir el siguiente
        continuar = input('Deseas hacer otro movimiento (s/n): ')
        if continuar == "s":
            
            while True:
                fo = int(input('Introduce la FILA de la pieza a mover: '))
                #fo es la fila origen
                co = int(input('Introduce la COLUMNA de la pieza a mover: '))
                #co es la columna origen
                pieza=tablero_inicial[fo][co]
                if  pieza != " ":
                    if movimiento%2 == 0 and Piezas.color_pieza(pieza)=="B":
                    #Está jugando en un movimiento par en el que juegan las blancas
                        break
                    elif movimiento%2 != 0 and pieza != " " and Piezas.color_pieza(pieza)=="N":
                    #Juegan las negras en los movimientos impares
                        break
                    else:
                        print("No es tu turno de juego")
                        #Está intentando jugar dos veces seguidas el mismo jugador.
                else:
                    print("La casilla seleccionada está vacia")

            while True:
                fd = int(input('Introduce la FILA de destino: '))
                #fd es la fila destino
                cd = int(input('Introduce la COLUMNA de destino: '))
                #cd es la columna destino
                if Piezas.posible_movimiento(tablero_inicial,fo,co,fd,cd,pieza) == True:
                    #Si el movimiento de pieza es posible se cambia la pieza de lugar
                    tablero_inicial[fo][co] = " "
                    #La casilla original pasa a estar vacia
                    tablero_inicial[fd][cd] = pieza
                    #La pieza ocupa la casilla de destino
                    movimiento += 1
                    #Añade un movimiento a esta variable
                    Ajedrez.añadir_tablero(tablero_inicial,nombre_fichero, movimiento)
                    #Añade el nuevo tablero con el último movimiento realizado
                    break
                else:
                    print("Movimiento no permitido")
                    break
        else:
            print("Hasta la próxima partida")
            break
    return
	
iniciar_partida("PartidaPrimera.txt")
#Inicia la partida almacenandola en el archivo que escribamos (PartidaPrimera.txt)