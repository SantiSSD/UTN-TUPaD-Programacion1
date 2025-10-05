#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a // b
    print("/////////////////////////")
    print("Operaciones Básicas")
    print(f"La suma de {a} + {b} es: {suma}\nLa resta de {a} - {b} es: {resta}\nLa Multiplicación de {a} * {b} es: {multiplicacion}\nY la División de {a} / {b} es: {division}")

#Programa Principal

n1 = int(input("Ingresa un primer numero: "))
n2 = int(input("Ingresa un segundo numero: "))

operaciones_basicas(n1,n2)