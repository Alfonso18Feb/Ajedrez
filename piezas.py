''''
clase que indica las accciones que pueden realizar las piezas
'''
class Piezas(object):
    '''
    funcion para mover las piezas
    Donde: fo=fila origen co=columna origen cd=columna destino fd=fila destino
    '''
    
    def mover_pieza(self,fo,co,fd,cd,pieza):
        self.fo=fo
        self.co=co
        self.fd=fd
        self.cd=cd
        self.pieza=pieza
       # self.color=color_pieza(pieza)
    """
    funcion que da el color de la pieza
    B es para Blanco
    N es para Negra
    """
    def color_pieza(pieza):
        if pieza=="♜" or pieza=="♞" or pieza=="♝" or pieza=="♛" or pieza=="♚" or pieza=="♟":
            color="B"
        else:
            color="N"
        return color
        #devuelve el color de la pieza
    '''
    función con todos los posibles movimientos de las piezas en el tablero de ajedrez
    '''
    def posible_movimiento(tablero_inicial,fo,co,fd,cd,pieza):
        #f = open(nombre_fichero, "r", encoding="utf8")

        if pieza=="♜" or pieza=="♖":
            return True
        elif pieza=="♞" or pieza=="♘":
            if (abs(fd-fo)==2 and abs(cd-co)==1) or (abs(fd-fo) == 1 and abs(cd-co) == 2):
            #define los movimientos posibles del caballo
                return True
            else:
                return False
        elif pieza=="♝" or pieza=="♗":
            return True
        elif pieza=="♛" or pieza=="♕":
            return True
        elif pieza=="♚" or pieza=="♔":
            if abs(cd-co)==1 or abs(fd-fo)==1:
            #define los movimientos posibles del rey
                return True
            else: 
                return False
        elif pieza=="♟":
            if cd-co == 0 and fd-fo ==2 or fd-fo==1 and tablero_inicial[fd+1][cd] == " ":
            #define los movimientos de los peones blancos
                return True
        elif pieza=="♙":
            if cd-co == 0 and fo-fd ==2 or fo-fd==1 and tablero_inicial[fd-1][cd] == " ":
            #define los movimientos de los peones negros
                return True
        else:
            #Movimiento no es posible
            return False