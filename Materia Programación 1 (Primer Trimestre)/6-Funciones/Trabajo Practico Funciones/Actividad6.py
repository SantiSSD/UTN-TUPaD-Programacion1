#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

def tabla_multiplicar(numero):
    print("///////////////////////////")
    print(f"La tabla de multiplicar de {numero}: ")
    for i in range (1, 11):
        tabla = numero * i  
        print(f"{numero} X {i} = {tabla}") 

#Programa Principal
numero = int(input("Ingrese un numero para ver su tabla del 1 al 10: "))

tabla_multiplicar(numero)

