'''
Objetos:
- '0' representa el personaje - "charac"
- '1' representa una caja - "box"
- '2' representa una meta - "goal"
- '3' representa una pared - "wall"
- '4' representa espacios/piso - "ground"
- '5' representa 
'''
import os
class Soko:

    map = [] # mapa del juego
    charac_column = 0
    charac_fila = 0
    box_column = 1
    box_fila = 1

    def __init__(self):
        # Define el mapa de juego
        self.map =[
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,4,0,4,4,4,4,4,4,4,1,4,2,3],
            [3,4,4,4,4,1,4,4,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,1,4,4,4,4,4,3],
            [3,4,4,4,4,4,4,4,4,4,4,4,4,3],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3]
        ]

        # Definimos la posicion inicial del personaje
        self.charac_column = 2
        self.charac_fila = 2
        # Definimos la posicion inicial de la caja #BORRAR------YAAAAA!#
        self.box_column = 10
        self.box_fila = 2

    def printMap(self):
        # Limpiar la pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        # Imprimir el mapa
        for fila in self.map:
            for numero in fila:
                if numero == 4:
                    print("  ", end=" ")
                elif numero == 0:  # Agrega esta condición para imprimir el personaje
                    print("🦠", end=" ")
                elif numero == 1:
                    print("📦", end=" ")
                elif numero == 2:
                    print("🏁", end=" ")
                else:
                    print("🚧" if numero == 3 else " ", end=" ")
            print()  # Imprime una nueva línea después de imprimir cada fila del mapa



#definir movimientos
    def mov1(self): #derecha - right
        # Donde estaba el personaje pone un piso
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba el piso pone al personaje
        self.map[self.charac_fila][self.charac_column + 1] = 0
        # Actualiza la posicion del personaje
        self.charac_column += 1

    def mov2(self): #izquierda - left
        # Donde estaba el personaje pone un piso
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba el piso pone al personaje
        self.map[self.charac_fila][self.charac_column - 1] = 0
        # Actualiza la posicion del personaje
        self.charac_column -= 1

    def mov3(self): #arriba - up
        # Donde estaba el personaje pone un piso
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba el piso pone al personaje
        self.map[self.charac_fila - 1][self.charac_column] = 0
        # Actualiza la posicion del personaje
        self.charac_fila -= 1

    def mov4(self): #abajo - down
        # Donde estaba el personaje pone un piso
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba el piso pone al personaje
        self.map[self.charac_fila + 1][self.charac_column] = 0
        # Actualiza la posicion del personaje
        self.charac_fila += 1

    def mov5(self): #right, caja [0,1,4]
        # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba la caja pone al personaje, [4,0,4]
        self.map[self.charac_fila][self.charac_column + 1] = 0
        # Donde estaba el piso pone a la caja
        self.map[self.charac_fila][self.charac_column + 2] = 1
        # Actualiza la posicion del personaje
        self.charac_column += 1

    def mov6(self): #left, caja [4,1,0]
        # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba la caja pone al personaje
        self.map[self.charac_fila][self.charac_column - 1] = 0
        # Donde estaba el piso pone a la caja
        self.map[self.charac_fila][self.charac_column - 2] = 1
        # Actualiza la posicion del personaje
        self.charac_column -= 1

    def mov7(self): #up, caja [4,1,0]
        # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba la caja pone al personaje
        self.map[self.charac_fila - 1][self.charac_column] = 0
        # Donde estaba el piso pone a la caja
        self.map[self.charac_fila - 2][self.charac_column] = 1
        # Actualiza la posicion del personaje
        self.charac_fila -= 1

    def mov8(self): #down, caja [4,1,0]
        # Donde estaba el personaje pone un piso, [4,0,4]
        self.map[self.charac_fila][self.charac_column] = 4
        # Donde estaba la caja pone al personaje
        self.map[self.charac_fila + 1][self.charac_column] = 0
        # Donde estaba el piso pone a la caja
        self.map[self.charac_fila + 2][self.charac_column] = 1
        # Actualiza la posicion del personaje
        self.charac_fila += 1


#movimientos
    def right(self):
        # Movimiento 1: [0,4] -> [4,0]
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 4:
            self.mov1()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column + 1] == 1) and self.map[self.charac_fila][self.charac_column + 2] == 4:
            self.mov5()

    def left(self):
        #mov 2: [4,0] -> [0,4]
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 4:
            self.mov2()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila][self.charac_column - 1] == 1) and self.map[self.charac_fila][self.charac_column - 2] == 4:
            self.mov6()

    def up(self):
        #mov 3: [4,4], [4,0] -> [4,0], [4,4]
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 4:
            self.mov3()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila - 1][self.charac_column] == 1) and self.map[self.charac_fila - 2][self.charac_column] == 4:
            self.mov7()

    def down(self):
        #mov 2: [4,0], [4,4] -> [4,4], [4,0]
        if self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 4:
            self.mov4()
        elif (self.map[self.charac_fila][self.charac_column] == 0 and self.map[self.charac_fila + 1][self.charac_column] == 1) and self.map[self.charac_fila + 2][self.charac_column] == 4:
            self.mov8()



    def play(self):
        while True:
            # Imprime el map
            self.printMap()
            # Pide al usuario el movimiento
            mov = input("Selecciona el mov: ")
            # Moverse a la derecha
            if mov == 'd':
                self.right()
            # Moverse a la izquierda
            if mov == 'a':
                self.left()
            # Moverse arriba
            if mov == 'w':
                self.up()
            # Moverse abajo
            if mov == 's':
                self.down()




soko = Soko()
soko.play()
