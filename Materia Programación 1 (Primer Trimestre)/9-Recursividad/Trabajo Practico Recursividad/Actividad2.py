def fibonacci_recursivo(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    else:
        return fibonacci_recursivo(num -1) + fibonacci_recursivo(num -2)
    

numero = int(input("Ingrese un numero :"))

for i in range (numero + 1):
    print(f"El termino fibonacci de {i} es {fibonacci_recursivo(i)}") 
