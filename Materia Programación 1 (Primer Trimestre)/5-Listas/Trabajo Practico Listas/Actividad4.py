# 4) Dada una lista con valores repetidos: 
# datos = [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 
datos = [1,3,5,3,7,1,9,5,3]


sin_repetidos = []
for dato in datos:

    if dato not in sin_repetidos:
        sin_repetidos.append(dato)

print("Numeros Con repetidos:")

for i in datos:
    print(i, end=" ")

print("\nNumeros sin repetidos:")
for i in sin_repetidos:
    
    print(i, end=" ")