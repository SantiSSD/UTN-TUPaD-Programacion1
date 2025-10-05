
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
import math

def calcular_area_circulo(radio):
    area = math.pi * radio **2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

#Programa principal

radio = float(input("Ingrese el radio para conocer el area y el perimetro de un circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es {area} y el perimetro es {perimetro}")

