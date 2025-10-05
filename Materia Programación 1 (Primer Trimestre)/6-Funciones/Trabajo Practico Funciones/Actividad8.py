#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

def calcular_imc(peso,altura):
    imc = peso / (altura **2)
    return imc

#Programa Principal

peso = float(input("Ingrese su peso por favor: "))
altura = float(input("Ingrese su altura por favor: "))

imc = calcular_imc(peso,altura)

print(f"Tu indice de masa corporal teniendo en cuenta tu peso {peso} y altura {altura} es de {imc:.2f}")