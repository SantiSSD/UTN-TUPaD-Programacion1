# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada.

tablero = []

for _ in range(3):
    fila = []
    for _ in range(3):
        fila.append("-")
    tablero.append(fila)

turno = 0
jugador_actual = "X"

while turno < 9:
    print(f"turno numero {turno}")
    print("\nTablero actual:")
    for f in range(3):
        print(tablero[f][0], tablero[f][1],tablero[f][2])

    print("\nJuega:", jugador_actual)
    fila_ing = int(input("Ingresa la FILA(1-3):")) - 1
    col_ing = int(input("Ingresá la COLUMNA (1-3): ")) - 1


    if fila_ing < 0  or fila_ing > 2 or col_ing < 0 or col_ing > 2:
        print("Posicion fuera de rango.Intentalo de nuevo")
        continue

    if tablero[fila_ing][col_ing] != "-":
        print("Casilla ocupada. Elegi Otra")
        continue

    #si paso las validaciones, colocamos la marca del jugador.
    tablero[fila_ing][col_ing] = jugador_actual
    turno+= 1

    #Mostramos el tablero luego de la jugada
    for f in range(3):
        print(tablero[f][0], tablero[f][1], tablero[f][2])
    

    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"
    