def piramide_bloques_recursivo(num):
    if num == 0:
        return 0
    else:
        return  num + piramide_bloques_recursivo(num - 1)
    
numero = int(input("Ingresa un número: "))

print(piramide_bloques_recursivo(numero))