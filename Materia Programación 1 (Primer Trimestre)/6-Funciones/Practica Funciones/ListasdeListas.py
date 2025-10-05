def agregar_elemento(matriz):
    matriz[0].append(99)
    matriz.append([4, 5, 6])

matriz = (
    [
    [1,2],
    [3,4]
    ]
        )
agregar_elemento(matriz)
print("Matriz final", matriz)