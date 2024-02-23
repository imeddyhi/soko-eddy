# soko-eddy
Implementación de sokoban en Python, versión retro consola

# SOKOBAN

#### Sokoban es un juego de rompecabezas clásico en el que el jugador controla a un personaje que debe empujar cajas hasta ubicarlas en destinos específicos dentro de un almacén. El desafío radica en planificar cuidadosamente los movimientos para evitar quedar atrapado o bloquear el camino de las cajas, ya que el espacio en el almacén es limitado y las cajas solo pueden empujarse, no jalar, además de obstáculos que perjudicaran o subirán el grado de complejidad de los niveles. Con niveles de dificultad creciente, Sokoban es un juego que pondrá a prueba tu ingenio y habilidades de resolución de problemas.

## ¿Cómo jugar sokoban?

**Objetos:**
- '0' representa el personaje
- '1' representa una caja
- '2' representa una meta
- '3' representa una pared
- '4' representa espacios/piso

1. **Movimiento del personaje**:
   El jugador controla un personaje que puede moverse horizontal o verticalmente (arriba, abajo, izquierda, derecha) a través del almacén. El personaje se mueve una casilla a la vez.
2. **Empujar cajas**:
   El personaje puede empujar una sola caja a la vez, siempre y cuando haya una casilla vacía en la dirección hacia la cual se desea empujar la caja.
3. **Abrir puertas**:
   Para permitir el paso a traves de puertas deberá mantener una caja sobre un botón de acción el tiempo que deberá estar abierta.
4. **Recolección de monedas**:
   Para recolectar monedas del juego deberá avanzar sobre el mapa y desplazarse sobre la moneda para que la cantidad indicada al momento de recolectarla se agregue a su bolsa de monedas. Verá la nueva suma fuera del mapa en el ícono de bolsa de dinero.
   
- El objetivo de cada nivel es empujar todas las cajas hasta ubicarlas en las casillas de destino. Estas casillas estarán marcadas con un símbolo especial como una estrella.

- *Restricciones*: No se puede empujar más de una caja al mismo tiempo, y tampoco se pueden jalar las cajas en ninguna dirección. Además, no se pueden empujar las cajas hacia fuera del área de juego ni sobre obstáculos fijos.

- *Bloqueos*: Si el jugador empuja una caja hacia una esquina o la coloca de manera que quede bloqueada contra una pared u otra caja, el nivel puede quedar irresoluble. En ese caso, el jugador deberá reiniciar el nivel o pagar por deshacer sus últimos movimientos.

- *Ayuda mínima*: Se evalúa la eficiencia del jugador en términos de la cantidad mínima de movimientos cancelados que pague para completar un nivel. Esto añade un desafío adicional y fomenta la optimización de la estrategia.

- *Niveles*: Sokoban ofrece una serie de niveles con dificultad progresiva, donde cada nivel introduce nuevas configuraciones y desafíos.


**Controles:**
Para jugar a Sokoban, utiliza los siguientes controles:

**Teclas de dirección:** Utiliza las flechas del teclado (arriba, abajo, izquierda, derecha) para mover al personaje en la dirección deseada.
Ejemplo:

W (Letra W): Mover hacia arriba.

S (Letra S): Mover hacia abajo.

A (Letra A): Mover hacia la izquierda.

D (Letra D): Mover hacia la derecha.

Q (Letra q): Deshacer último movimiento.

X (Letra x): Salir.

| Encabezado 1 | Encabezado 2 | Encabezado 3 |
|--------------|--------------|--------------|
| Celda 1      | Celda 2      | Celda 3      |
| Celda 4      | Celda 5      | Celda 6      |

[Adobe](https://www.adobe.com)
See [Overview example article](../../overview.md)
