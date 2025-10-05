# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

def calcular_promedio(a, b, c):
    promedio = (a+b+c) / 3
    return promedio

#Programa Principal

n1 = int(input("Ingrese un primer número: "))
n2 = int(input("Ingrese un segundo número: "))
n3 = int(input("Ingrese un tercer número: "))

promedio = calcular_promedio(n1,n2,n3)

print(f"El promedio de los numero {n1}, {n2} y {n3} es de: {promedio}")