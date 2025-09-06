numero = int(input("Ingrese un numero entero para invertirlo porfavor"))

while numero != 0:
    ultimo = numero % 10
    resultado = print(ultimo, end="")
    numero = numero // 10


