numero1 = int(input("Ingrese el primer numero"))
numero2 = int(input("Ingrese el segundo numero"))
suma = 0

if numero1 > numero2:
    aux = numero1
    numero1 = numero2
    numero2 = aux

for i in range(numero1 + 1, numero2):
    print(f"Numero comprendido {i}")
    suma = suma + i

print(f"la suma de los números comprendidos es {suma}")