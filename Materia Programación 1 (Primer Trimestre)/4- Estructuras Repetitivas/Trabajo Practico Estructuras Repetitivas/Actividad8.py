pares = 0
impares = 0
negativos = 0
positivos = 0
contador = 0
while contador != 100:
    numero = int(input("Ingrese un numero por favor"))
    contador += 1
    if numero >= 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    if numero % 2 != 0:
        impares += 1

print(f"La cantidad de números pares son {pares}, de impares son {impares}, de positivos {positivos} y de negativos {negativos}")
    
