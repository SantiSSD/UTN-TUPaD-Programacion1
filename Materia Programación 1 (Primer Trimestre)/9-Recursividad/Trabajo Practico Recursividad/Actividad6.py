def suma_digitos_recursivo(num):
    if num == 0:
        return 0
    else:
        return num % 10 + suma_digitos_recursivo(num // 10)
    

numero = int(input("Ingresa un numero para sumar sus digitos: "))

print(suma_digitos_recursivo(numero))