**soko-by-eddy**
Implementación de sokoban en Python, versión retro consola

# SOKOBAN

#### Sokoban es un juego de rompecabezas clásico en el que el jugador controla a un personaje que debe empujar cajas hasta ubicarlas en destinos específicos dentro de un almacén. El desafío radica en planificar cuidadosamente los movimientos para evitar quedar atrapado o bloquear el camino de las cajas, ya que el espacio en el almacén es limitado y las cajas solo pueden empujarse, no jalar, además de obstáculos que perjudicaran o subirán el grado de complejidad de los niveles. Con niveles de dificultad creciente, Sokoban es un juego que pondrá a prueba tu ingenio y habilidades de resolución de problemas.

## 1. Objetivo

### 1.1 General

Programar el juego Sokoban en una versión retro para consola.

### 1.2 Específicos

- Aplicar los conocimientos básicos de programación orientada a objetos  con python (Clases, Objetos, Métodos, Variables, Arrays, Bucles, Leer desde teclado, Decisiones, etc.).

- Utilizar ingeniería de software para analizar, diseñar y desarrollar el juego.

- Utilizar Kanban para dar seguimeinto a las actividades a realizar ToDo, Doing, Done.

- Utilizar Hitos (Milestones) para cada una de las etapas del desarrollo.

## 2. Reglas del juego

El juego sokoban consiste en recorrer un mapa para acomodar cajas en puntos determinados por las metas, y tiene las siguientes reglas:

1. El personaje se puede mover hacia arriba, abajo, izquierda y derecha.
2. El personaje solo puede empujar 1 caja hacia arriba, abjo, izquierda o derecha.
3. El personaje se moverá en un mapa predefinido.
4. Para terminar el nivel se tienen que acomodar todas las cajas sobre las metas.
5. Cada nivel tiene distinto número de cajas y metas.
6. El nivel de dificultad no está determinado necesariamente por la cantidad de cajas y metas.
7. Abrir puertas: Para permitir el paso a traves de puertas deberá mantener una caja sobre un botón de acción el tiempo que deberá estar abierta.
8. Recolección de monedas: Para recolectar monedas del juego deberá avanzar sobre el mapa y desplazarse sobre la moneda para que la cantidad indicada al momento de recolectarla se agregue a su bolsa de monedas. Verá la nueva suma fuera del mapa en el ícono de bolsa de dinero.

## 3. Elementos del juego

Sokoban tiene 2 partes principales de juego, el mapa donde se va jugar y los elementos (personaje, cajas, metas, paredes y piso).

### 3.1 Mapa de juego

Cada nivel del juego se colocará dentro de una array bidimensional, colocando números para representar los elementos de juego, a continuación se tiene un ejemplo básico de nivel.

````code
mapa = [
            [3,3,3,3,3,3,3],
            [3,4,4,4,4,4,3],
            [3,4,0,4,1,2,3],
            [3,4,4,4,4,4,3],
            [3,3,3,3,3,3,3]
        ]
````

### 3.2 Lista de elementos

- 0 - Personaje
- 1 - Cajas
- 2 - Metas
- 3 - Paredes
- 4 - Piso
- 5 - Pesonaje_meta
- 6 - Caja_meta

## 4. Controles

Para moverse en el juego el usuario utilizará alguna de las siguientes letras para indicar hacia adonde se quiere mover:

- a -> Izquierda
- s -> Derecha
- w -> Arriba
- s -> Abajo
- q -> Deshacer último movimiento

Nota: El proceso es que se muestra el mapa y se solicita al usuario que escriba la letra hacia donde se quiere mover, despúes de colocar la letra se preciona enter y se actualiza el mapa, este proceso se repite de forma infinita.


## 5. Función a implementar

Para llevar un mejor control del avance del desarrollo llenar Kanban con los siguientes elementos (ToDo, Doing y Done).

| No. |Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 0. | Cargar el siguiente nivel. | - | - |
| 1. | Repetir el juego hasta terminar el nivel. | Done | Mars, 12, 2024 |
| 2. | Imprimir mapa.| Done | - |
| 3. | Leer el movimiento. | Done | - |
| 4. | Evaluar el movimiento del usuario. | Done | - |

## Derecha

Ejemplo de movimientos Inicio y Fin:

- Personaje, Espacio [0,4] -> Espacio, Personaje [4,0] |


| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 5. | Personaje, espacio  | Done | [0,4] | [4,0] | - |
| 6. | Personaje, meta  | Done | [0,2] | [4,5] | April 5, 2024 |
| 7. | Personaje, caja, espacio | Done | [0,1,4] | [4,0,1] | - |
| 8. | Personaje, caja,  meta | Done | [0,1,2] | [4,0,6] | Mars 22, 2024 |
| 9. | Personaje, caja_meta, espacio | Done | [0,6,4] | [4,5,1] | April 5, 2024 |
| 10. | Personaje, caja_meta, meta | Done | [0,6,2] | [4,5,6] | April 9, 2024 |
| 11. | Personaje_meta, espacio | Done | [5,4] | [2,0] | April 5, 2024 |
| 12. | Personaje_meta, meta | Done | [5,2] | [2,5] | April 9, 2024 |
| 13. | Personaje_meta, caja, espacio | Done | [5,1,4] | [2,0,1] | April 5, 2024 |
| 14. | Personaje_meta, caja, meta | Done | [5,1,2] | [2,0,6] | April 9, 2024 |
| 15. | Personaje_meta, caja_meta, espacio | Done | [5,6,4] | [2,5,1] | April 9, 2024 |
| 16. | Personaje_meta, caja_meta, meta | Done | [5,6,2] | [2,5,6] | April 9, 2024 |

## Izquierda

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 17. | Personaje, espacio | Done | [4,0] | [0,4] | - |
| 18. | Personaje, meta | Done | [2,0] | [5,4] | April 5, 2024 |
| 19. | Personaje, caja, espacio | Done | [4,1,0] | [1,0,4] | - |
| 20. | Personaje, caja, meta | Done | [2,1,0] | [6,0,4] | Mars 22, 2024 |
| 21. | Personaje, caja_meta, espacio | Done | [4,6,0] |[1,5,4] | April 5, 2024 |
| 22. | Personaje, caja_meta, meta | Done | [2,6,0] | [6,5,4] | April 9, 2024 |
| 23. | Personaje_meta, espacio | Done | [4,5] | [0,2] | April 5, 2024 |
| 24. | Personaje_meta, meta | Done | [2,5] | [5,2] | April 9, 2024 |
| 25. | Personaje_meta, caja, espacio | Done | [4,1,5] | [1,0,2] | April 5, 2024 |
| 26. | Personaje_meta, caja, meta | Done | [2,1,5] | [6,0,2] | April 9, 2024 |
| 27. | Personaje_meta, caja_meta, espacio | Done | [4,6,5] | [1,5,2] | April 9, 2024 |
| 28. | Personaje_meta, caja_meta, meta | Done | [2,6,5] | [6,5,2] | April 9, 2024 |

## Arriba

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 29. | Personaje, espacio | Done | [4][0] | [0][4] | - |
| 30. | Personaje, meta | Done | [2][0] | [5][4] | April 5, 2024 |
| 31. | Personaje, caja, espacio | Done | [4][1][0] | [1][0][4] | - |
| 32. | Personaje, caja, meta | Done | [2][1][0] | [6][0][4] | - |
| 33. | Personaje, caja_meta, espacio | Done | [4][6][0] | [1][5][4] | April 5, 2024 |
| 34. | Personaje, caja_meta, meta | Done | [2][6][0] | [6][5][4] | April 9, 2024 |
| 35. | Personaje_meta, espacio | Done | [4][5] | [0][2] | - |
| 36. | Personaje_meta, meta | Done | [2][5] | [5][2] | April 9, 2024 |
| 37. | Personaje_meta, caja, espacio | Done | [4][1][5] | [1][0][2] | April 5, 2024 |
| 38. | Personaje_meta, caja, meta | Done | [2][1][5] | [6][0][2] | April 9, 2024 |
| 39. | Personaje_meta, caja_meta, espacio | Done | [4][6][5] | [1][5][2] | April 9, 2024 |
| 40. | Personaje_meta, caja_meta, meta | Done | [2][6][5] | [6][5][2] | April 9, 2024 |

## Abajo

| No. | Función | Kanban | Inicio | Fin | Fecha terminación |
| --- | --- | --- | --- | --- | --- |
| 41. | Personaje, espacio | Done | [0][4] | [4][0] | - |
| 42. | Personaje, meta | Done | [0][2] | [4][5] | April 5, 2024 |
| 43. | Personaje, caja, espacio | Done | [0][1][4] | [4][0][1] | - |
| 44. | Personaje, caja, meta | Done | [0][1][2] | [4][0][6] | - |
| 45. | Personaje, caja_meta, espacio | Done | [0][6][4] | [4][5][1] | April 5, 2024 |
| 46. | Personaje, caja_meta, meta | Done | [0][6][2] | [4][5][6] | April 9, 2024 |
| 47. | Personaje_meta, espacio | Done | [5][4] | [2][0] | April 5, 2024 |
| 48. | Personaje_meta, meta | Done | [5][2] | [2][5] | April 9, 2024 |
| 49. | Personaje_meta, caja, espacio | Done | [5][1][4] | [2][0][1] | April 5, 2024 |
| 50. | Personaje_meta, caja, meta | Done | [5][1][2] | [2][0][6] | April 9, 2024 |
| 51. | Personaje_meta, caja_meta, espacio | Done | [5][6][4] | [2][5][1] | April 9, 2024 |
| 52. | Personaje_meta, caja_meta, meta | Done | [5][6][2] | [2][5][6] | April 9, 2024 |

## Determina si se completo el nivel o no

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 53. | Evaluar si el nivel esta terminado (Esto sucede cuando todas las cajas estan sobre las metas), SI el nivel esta terminado cargar el siguiente nivel (Los niveles de juego estarán en archivos de texto independiente). | - | - |
| 54. | Reiniciar el mapa (Con la letra r, se vuelve a cargar el nivel que se esta jugando) | Done | April 9, 2024 |

## Función extra

| No. | Función | Kanban | Fecha terminación |
| --- | --- | --- | --- |
| 55. | Función adicional o powerup (descripción). | - | - |

