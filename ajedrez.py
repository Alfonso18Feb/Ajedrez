'''
clase que recoje las acciones a realizar dentro del tablero de ajedrez
'''
class Ajedrez(object):
    
    ''' Función (imprimir_tablero) que muestra por pantalla el tablero n de una partida de ajedrez. 
        Toma los valores (nombre_fichero) con todos los tableros de la partida 
        y (n) con el número del tablero que se tiene que mostrar.'''
    def imprimir_tablero(nombre_fichero, n):
        f = open(nombre_fichero, "r", encoding="utf8")
        # Abre el fichero (nombre_fichero) en modo lectura (r)
        tableros = f.read().split('\n')
        # Lee el contenido y lo guardamos en (tableros) dividiendo la cadena por el caracter de cambio de línea.
        for i in range(9*n,9*n+8):
            #En función del numero de tablero son múltiplos de 8
            print (tableros[i])
            #Imprime las 8 cadenas de la jugada.
        return

    ''' Función (añadir_tablero) que añade un tablero con el último movimiento realizado. 
        Toma los valores (tablero_inicial) que contiene el último movimiento de la partida,
        (nombre_fichero) con todos los tableros anteriores
        y (n) con el número del tablero a añadir.'''
    def añadir_tablero(tablero_inicial, nombre_fichero, n):
        f = open(nombre_fichero, "a", encoding="utf8")
        # Abre el fichero (nombre_fichero) en modo añadir (a)
        f.write('Movimiento' + str(n) + '\n')
        #Escribe el número de movimiento para diferenciar cada tablero.
        for i in range(8):
            for j in range(8):
                f.write(tablero_inicial[i][j]+"\t")
            f.write("\n")
        f.close
        return
    
#imprimir_tablero("PartidaPrimera.txt", 0)
#Línea anterior para hacer pruebas del buen funcionamiento