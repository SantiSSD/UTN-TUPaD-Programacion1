def factorial_recursivo(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recursivo(num -1)

numero = int(input("Ingresa un numero: "))
for i in range(numero +1):
    print(f"El factorial de {i} es {factorial_recursivo(i)} ")


