suma = 0 
contador = 0
promedio = 0

while contador != 100:
    numero = int(input("Ingrese un numero entero"))
    suma += numero
    contador += 1

promedio = suma / contador

print(f"La media de los {contador} valores enteros es {promedio}")