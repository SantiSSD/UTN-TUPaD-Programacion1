#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Programa Principal

celsius = float(input("Ingresa una temperatura en grados Celsius para convertirlos a grados Fahrenheit: "))

conversion = celsius_a_fahrenheit(celsius)

print(f"La conversión de {celsius} grados celsius es de {conversion} grados Fahrenheit")