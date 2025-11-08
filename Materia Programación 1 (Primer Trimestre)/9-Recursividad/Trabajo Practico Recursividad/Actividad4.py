def conversion_binario(num):
    if num == 0:
        return ""
    else:
        return conversion_binario(num// 2) + str(num % 2)
         

numero = int(input("Ingresa un número para convertirlo en binario por favor: "))

print(f"El numero binario para el numero decimal {numero} es {conversion_binario(numero)}")