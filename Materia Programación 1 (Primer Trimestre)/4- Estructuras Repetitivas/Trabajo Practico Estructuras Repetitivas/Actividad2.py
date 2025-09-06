numero = int(input("Ingrese un número entero porfavor"))

digito = 0

while numero > 0:
    numero = numero // 10
    digito += 1

print(f"la cantidad de digitos es de {digito} digitos")

