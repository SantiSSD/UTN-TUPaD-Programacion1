# Creamos e inicializamos la lista con valores desordenados 

# lista = [23,34,23,12,21,2,23,]
lista = [1,2,3,4,5,6,7,8,9,10]

print("Lista Original")
print(lista)

cantidad_elementos = len(lista)
print(cantidad_elementos)

for indice_pasada in range(cantidad_elementos - 1):
    print(f"Recorrido = {indice_pasada + 1}")
    hizo_intercambio = False
    for indice_actual in range (cantidad_elementos - 1 - indice_pasada):
        if lista[indice_actual] > lista[indice_actual + 1]:
            lista[indice_actual], lista[indice_actual + 1] = lista[indice_actual + 1], lista[indice_actual]
            hizo_intercambio = True
    if hizo_intercambio == False:
        break
print("Lista ordenada de menor a mayor")
print(lista)