import random
intentos = 0
numero_aleatorio = random.randint(0,9)
numero = 0
print(numero_aleatorio)
while numero != numero_aleatorio:
        
        numero = int(input("Ingrese un número del 0 al 9"))
        intentos += 1

print(f"Se necesitaron {intentos} intentos para encontra el numero {numero_aleatorio}")