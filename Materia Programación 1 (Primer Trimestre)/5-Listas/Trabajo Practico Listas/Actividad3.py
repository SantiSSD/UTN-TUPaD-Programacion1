# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

import random
numeros_azar = []
for i in range(15):
    numeros = random.randint(1, 100)
    numeros_azar.append(numeros)

lista_pares = []
lista_impares = []
for i in numeros_azar:
    if i % 2 == 0:
        lista_pares.append(i)
    elif i % 2 != 0:
        lista_impares.append(i)

print(f"la cantidad de numeros pares son {len(lista_pares)} \nla cantidad de numeros impares es {len(lista_impares)}")

print("Lista de pares")

for pares in lista_pares:
    print(pares, end=" ")

print("\nLista de Impares")

for impares in lista_impares:
    print(impares, end=" ")