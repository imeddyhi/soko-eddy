'''
Objetos:
- '0' representa el personaje - "charac"
- '1' representa una caja - "box"
- '2' representa una meta - "goal"
- '3' representa una pared - "wall"
- '4' representa espacios/piso - "ground"
- '5' representa el personaje sobre meta - "charac-goal"
- '6' representa una caja sobre meta - "box-goal"
'''
import os
class Soko:

    map = [] # mapa del juego
    charac_column = 0
    charac_fila = 0
    box_column = 1
    box_fila = 1

    def __init__(self): # Define el mapa de juego
        self.map =[
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,0,4,2,2,4,4,4,4,1,4,2,3],
            [3,4,4,2,2,1,2,4,4,4,4,4,4,3],
            [3,4,4,4,4,2,4,1,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.charac_column = 2
        self.charac_fila = 3

    def printMap(self): # Imprimir el mapa
        os.system('cls' if os.name == 'nt' else 'clear') # Limpiar la pantalla
        for fila in self.map:
            for numero in fila:
                if numero == 4:
                    print("  ", end=" ")
                elif numero == 0:  # Agrega esta condición para imprimir el personaje
                    print("😼", end=" ")
                elif numero == 1:
                    print("📦", end=" ")
                elif numero == 2:
                    print("🏁", end=" ")
                elif numero == 5:
                    print("😺", end=" ")
                elif numero == 6:
                    print("🏴", end=" ")
                elif numero == 3:
                    print("🚧", end=" ")
            print()  # Imprime una nueva línea después de imprimir cada fila del mapa
        boxes = sum(fila.count(1) for fila in self.map)  # Contamos el número de cajas en el mapa
        print("Cajas restantes: ", boxes)

#definir movimientos
    def mov1(self): #derecha - right, [0,4] -> [4,0]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso
        self.map[self.charac_fila][self.charac_column + 1] = 0 # Donde estaba el piso pone al personaje
        self.charac_column += 1 # Actualiza la posicion del personaje

    def mov2(self): #izquierda - left [4,0] -> [0,4]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso
        self.map[self.charac_fila][self.charac_column - 1] = 0 # Donde estaba el piso pone al personaje
        self.charac_column -= 1 # Actualiza la posicion del personaje

    def mov3(self): #arriba - up [4][0] -> [0][4]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso
        self.map[self.charac_fila - 1][self.charac_column] = 0 # Donde estaba el piso pone al personaje
        self.charac_fila -= 1 # Actualiza la posicion del personaje

    def mov4(self): #abajo - down [0][4] -> [4][0]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso
        self.map[self.charac_fila + 1][self.charac_column] = 0 # Donde estaba el piso pone al personaje
        self.charac_fila += 1 # Actualiza la posicion del personaje

    def mov5(self): #right, caja [0,1,4] -> [4,0,1]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila][self.charac_column + 1] = 0 # Donde estaba la caja pone al personaje, [4,0,4]
        self.map[self.charac_fila][self.charac_column + 2] = 1 # Donde estaba el piso pone a la caja
        self.charac_column += 1

    def mov6(self): #left, caja [4,1,0] -> [1,0,4]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila][self.charac_column - 1] = 0 # Donde estaba la caja pone al personaje
        self.map[self.charac_fila][self.charac_column - 2] = 1 # Donde estaba el piso pone a la caja
        self.charac_column -= 1 

    def mov7(self): #up, caja [4][1][0] -> [1][0][4]
        self.map[self.charac_fila][self.charac_column] = 4 # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila - 1][self.charac_column] = 0 # Donde estaba la caja pone al personaje
        self.map[self.charac_fila - 2][self.charac_column] = 1 # Donde estaba el piso pone a la caja
        self.charac_fila -= 1

    def mov8(self): #down, caja [0][1][4] -> [4][0][1]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila + 1][self.charac_column] = 0
        self.map[self.charac_fila + 2][self.charac_column] = 1
        self.charac_fila += 1

    def mov9(self): #right, box-goal [0,1,2] -> [4,0,6]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column + 1] = 0
        self.map[self.charac_fila][self.charac_column + 2] = 6 # Donde estaba la meta pone una caja sobre meta
        self.charac_column += 1

    def mov10(self): #left, box-goal [2,1,0] -> [6,0,4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column - 1] = 0
        self.map[self.charac_fila][self.charac_column - 2] = 6
        self.charac_column -= 1

    def mov11(self): #up, box-goal [2][1][0] -> [6][0][4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila - 1][self.charac_column] = 0
        self.map[self.charac_fila - 2][self.charac_column] = 6
        self.charac_fila -= 1

    def mov12(self): #down, box-goal [0][1][2] -> [4][0][6]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila + 1][self.charac_column] = 0
        self.map[self.charac_fila + 2][self.charac_column] = 6
        self.charac_fila += 1

    def mov13(self): #right, box-goal->ground [0,6,4] -> [4,5,1]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column + 1] = 5 # Donde estaba caja sobre meta pone personaje sobre meta
        self.map[self.charac_fila][self.charac_column + 2] = 1
        self.charac_column += 1

    def mov14(self): #left, box-goal->ground [4,6,0] -> [1,5,4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column - 1] = 5 
        self.map[self.charac_fila][self.charac_column - 2] = 1
        self.charac_column -= 1

    def mov15(self): #up, box-goal->ground [4][6][0] -> [1][5][4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila - 1][self.charac_column] = 5 
        self.map[self.charac_fila - 2][self.charac_column] = 1
        self.charac_fila -= 1

    def mov16(self): #down, box-goal->ground [0][6][4] -> [4][5][1]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila + 1][self.charac_column] = 5 
        self.map[self.charac_fila + 2][self.charac_column] = 1
        self.charac_fila += 1

    def mov17(self): #right, box-goal-ground [5,1,4] -> [2,0,1]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column + 1] = 0
        self.map[self.charac_fila][self.charac_column + 2] = 1
        self.charac_column += 1

    def mov18(self): #left, box-goal-ground [4,1,5] -> [1,0,2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column - 1] = 0
        self.map[self.charac_fila][self.charac_column - 2] = 1
        self.charac_column -= 1

    def mov19(self): #up, box-goal-ground [4][1][5] -> [1][0][2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila - 1][self.charac_column] = 0
        self.map[self.charac_fila - 2][self.charac_column] = 1
        self.charac_fila -= 1

    def mov20(self): #down, box-goal-ground [5][1][4] -> [2][0][1]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila + 1][self.charac_column] = 0
        self.map[self.charac_fila + 2][self.charac_column] = 1
        self.charac_fila += 1

    def mov21(self): #right->goal, [0,2] -> [4,5]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column + 1] = 5 # Donde estaba la meta pone al personaje sobre meta
        self.charac_column += 1

    def mov22(self): #left->goal [2,0] -> [5,4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column - 1] = 5
        self.charac_column -= 1

    def mov23(self): #up->goal [2][0] -> [5][4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila - 1][self.charac_column] = 5
        self.charac_fila -= 1

    def mov24(self): #down->goal [0][2] -> [4][5]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila + 1][self.charac_column] = 5
        self.charac_fila += 1

    def mov25(self): #right goal->ground, [5,4] -> [2,0]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column + 1] = 0
        self.charac_column += 1

    def mov26(self): #left goal->groung, [4,5] -> [0,2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column - 1] = 0
        self.charac_column -= 1

    def mov27(self): #up goal->ground, [4][5] -> [0][2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila - 1][self.charac_column] = 0
        self.charac_fila -= 1

    def mov28(self): #down goal->ground, [5][4] -> [2][0]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila + 1][self.charac_column] = 0
        self.charac_fila += 1

    def mov29(self): #right, box-goal-goal [0,6,2] -> [4,5,6]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column + 1] = 5
        self.map[self.charac_fila][self.charac_column + 2] = 6
        self.charac_column += 1

    def mov30(self): #left, box-goal-goal [2,6,0] -> [6,5,4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila][self.charac_column - 1] = 5
        self.map[self.charac_fila][self.charac_column - 2] = 6
        self.charac_column -= 1

    def mov31(self): #up, box-goal-goal Done [2][6][0] -> [6][5][4]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila - 1][self.charac_column] = 5
        self.map[self.charac_fila - 2][self.charac_column] = 6
        self.charac_fila -= 1

    def mov32(self): #down, box-goal-goal [0][6][2] -> [4][5][6]
        self.map[self.charac_fila][self.charac_column] = 4
        self.map[self.charac_fila + 1][self.charac_column] = 5
        self.map[self.charac_fila + 2][self.charac_column] = 6
        self.charac_fila += 1

    def mov33(self): #right charac-goal->goal, [5,2] -> [2,5]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column + 1] = 5
        self.charac_column += 1

    def mov34(self): #left charac-goal->goal, [2,5] -> [5,2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column - 1] = 5
        self.charac_column -= 1

    def mov35(self): #up goal->ground, [2][5] -> [5][2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila - 1][self.charac_column] = 5
        self.charac_fila -= 1

    def mov36(self): #down goal->ground, [5][2] -> [2][5]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila + 1][self.charac_column] = 5
        self.charac_fila += 1
    
    def mov37(self): #right, charac-goal-box-goal [5,1,2] -> [2,0,6]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column + 1] = 0
        self.map[self.charac_fila][self.charac_column + 2] = 6
        self.charac_column += 1

    def mov38(self): #left, charac-goal-box-goal [2,1,5] -> [6,0,2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila][self.charac_column - 1] = 0
        self.map[self.charac_fila][self.charac_column - 2] = 6
        self.charac_column -= 1

    def mov39(self): #up, charac-goal-box-goal [2][1][5] -> [6][0][2]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila - 1][self.charac_column] = 0
        self.map[self.charac_fila - 2][self.charac_column] = 6
        self.charac_fila -= 1

    def mov40(self): #down, charac-goal-box-goal [5][1][2] -> [2][0][6]
        self.map[self.charac_fila][self.charac_column] = 2
        self.map[self.charac_fila + 1][self.charac_column] = 0
        self.map[self.charac_fila + 2][self.charac_column] = 6
        self.charac_fila += 1

#movimientos
    def right(self): # Movimiento del personaje a la derecha
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 4:
            self.mov1()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 1 and self.map[self.charac_fila][self.charac_column + 2] == 4):
            self.mov5()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 1 and self.map[self.charac_fila][self.charac_column + 2] == 2):
            self.mov9()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 6 and self.map[self.charac_fila][self.charac_column + 2] == 4):
            self.mov13()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column + 1] == 1 and self.map[self.charac_fila][self.charac_column + 2] == 4):
            self.mov17()
        elif self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 2:
            self.mov21()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column + 1] == 4:
            self.mov25()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 6 and self.map[self.charac_fila][self.charac_column + 2] == 2):
            self.mov29()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column + 1] == 2:
            self.mov33()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column + 1] == 1 and self.map[self.charac_fila][self.charac_column + 2] == 2):
            self.mov37()

    def left(self): # Movimiento del personaje a la izquierda
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 4:
            self.mov2()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 1 and self.map[self.charac_fila][self.charac_column - 2] == 4):
            self.mov6()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 1 and self.map[self.charac_fila][self.charac_column - 2] == 2):
            self.mov10()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 6 and self.map[self.charac_fila][self.charac_column - 2] == 4):
            self.mov14()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column - 1] == 1 and self.map[self.charac_fila][self.charac_column - 2] == 4):
            self.mov18()
        elif self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 2:
            self.mov22()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column - 1] == 4:
            self.mov26()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 6 and self.map[self.charac_fila][self.charac_column - 2] == 2):
            self.mov30()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column - 1] == 2:
            self.mov34()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila][self.charac_column - 1] == 1 and self.map[self.charac_fila][self.charac_column - 2] == 2):
            self.mov38()

    def up(self): # Movimiento del personaje arriba
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 4:
            self.mov3()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 1 and self.map[self.charac_fila - 2][self.charac_column] == 4):
            self.mov7()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 1 and self.map[self.charac_fila - 2][self.charac_column] == 2):
            self.mov11()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 6 and self.map[self.charac_fila - 2][self.charac_column] == 4):
            self.mov15()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila - 1][self.charac_column] == 1 and self.map[self.charac_fila - 2][self.charac_column] == 4):
            self.mov19()
        elif self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 2:
            self.mov23()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila - 1][self.charac_column] == 4:
            self.mov27()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 6 and self.map[self.charac_fila - 2][self.charac_column] == 2):
            self.mov31()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila - 1][self.charac_column] == 2:
            self.mov35()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila - 1][self.charac_column] == 1 and self.map[self.charac_fila - 2][self.charac_column] == 2):
            self.mov39()

    def down(self): # Movimiento del personaje abajo
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 4:
            self.mov4()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 1 and self.map[self.charac_fila + 2][self.charac_column] == 4):
            self.mov8()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 1 and self.map[self.charac_fila + 2][self.charac_column] == 2):
            self.mov12()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 6 and self.map[self.charac_fila + 2][self.charac_column] == 4):
            self.mov16()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila + 1][self.charac_column] == 1 and self.map[self.charac_fila + 2][self.charac_column] == 4):
            self.mov20()
        elif self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 2:
            self.mov24()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila + 1][self.charac_column] == 4:
            self.mov28()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 6 and self.map[self.charac_fila + 2][self.charac_column] == 2):
            self.mov32()
        elif self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila + 1][self.charac_column] == 2:
            self.mov36()
        elif (self.map[self.charac_fila][self.charac_column] == 5 and self.map[self.charac_fila + 1][self.charac_column] == 1 and self.map[self.charac_fila + 2][self.charac_column] == 2):
            self.mov40()

#lectura de teclado
    def play(self):
        while True:
            self.printMap() # Imprime el map
            mov = input("Selecciona el mov: ") # Pide al usuario el movimiento
            if mov == 'd': # Moverse a la derecha con letra d
                self.right()
            if mov == 'a': # Moverse a la izquierda con letra a
                self.left()
            if mov == 'w': # Moverse arriba con letra w
                self.up()
            if mov == 's': # Moverse abajo con letra s
                self.down()

soko = Soko()
soko.play()
