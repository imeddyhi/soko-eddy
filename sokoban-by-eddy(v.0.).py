'''
Versión de sokoban de eduardo
version 0 (thu-02-22-2024)
'''

# '0' representa el personaje
# '1' representa una caja
# '2' representa una meta
# '3' representa una pared
# '4' representa espacios/piso

mapa = [3,4,4,0,4,4,4,3] # Se asigna un array a la variable mapa, crea una fila con 8 columnas donde el personaje podrá moverse laterlamente
posicion_personaje = mapa.index(0) # index busca la posición de 0(personaje) en la variable mapa y la asigna a la variable posicion_personaje

# Mostrar el mapa inicial
print("Mapa del almacén:")
print(mapa)

# Bucle principal del juego
while True:
    # Mostrar el mapa del almacén con la posición actual del personaje
    for casilla in mapa:
        print(casilla, end=' ')
    print()

# Pedir al usuario que presione una tecla para mover al personaje
    tecla = input("Presiona 'd' o 'a' para mover al personaje a la derecha o izquierda (o 'x' para salir): ").lower()

# Mover al personaje según la tecla presionada
    if tecla == 'd':
        if posicion_personaje < len(mapa) - 1 and mapa[posicion_personaje + 1] in [4, 2]:
            mapa[posicion_personaje] = 4
            mapa[posicion_personaje + 1] = 0
            posicion_personaje += 1

    if tecla == 'a':
        if posicion_personaje < len(mapa) + 1 and mapa[posicion_personaje - 1] in [4, 2]:
            mapa[posicion_personaje] = 4
            mapa[posicion_personaje - 1] = 0
            posicion_personaje -= 1

    elif tecla == 'x': # Envía un mensaje de despedida al presionar tecla x
        print("¡Hasta luego!")
        break
