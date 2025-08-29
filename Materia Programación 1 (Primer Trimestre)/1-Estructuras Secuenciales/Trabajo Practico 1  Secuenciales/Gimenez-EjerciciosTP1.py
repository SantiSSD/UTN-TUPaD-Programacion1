# Trabajo Practico N°1 Secuenciales
# Alumno: Cristhian Santiago Gimenez

# Ejercicio 1:
print("Hola Mundo!")

# Ejercicio 2:

Nombre = input("Ingrese su nombre porfavor!") 
print(f"Hola {Nombre}!! ")

# Ejercicio 3:
Nombre = input("Ingrese su nombre")
Apellido = input("Ingrese su apellido")
Edad = int(input("Ingrese su edad"))
Residencia = input("Ingrese su lugar de residencia")

print(f"Soy {Nombre} {Apellido}, tengo {Edad} años y vivo en {Residencia}")

# Ejercicio 4:
pi = 3.14159
Radio = float(input("Ingrese el radio de un circulo porfavor:"))
Area = pi * Radio ** 2
Perimetro = 2 * pi * Radio

print(f"El area del circulo es {Area}, y su perimetro es {Perimetro}")

# Ejercicio 5:

Segundos = int(input("Ingrese la cantidad de segundos"))
Horas =  Segundos / 3600

print(f" {Segundos} segundos equivale a {horas} horas")

# Ejercicio 6

Numero = int(input("Ingrese un número para saber su tabla de multiplicar"))
print(f"{Numero} x 1 = {Numero * 1}")
print(f"{Numero} x 2 = {Numero * 2}")
print(f"{Numero} x 3 = {Numero * 3}")
print(f"{Numero} x 4 = {Numero * 4}")
print(f"{Numero} x 5 = {Numero * 5}")
print(f"{Numero} x 6 = {Numero * 6}")
print(f"{Numero} x 7 = {Numero * 7}")
print(f"{Numero} x 8 = {Numero * 8}")
print(f"{Numero} x 9 = {Numero * 9}")
print(f"{Numero} x 10 = {Numero * 10}")

# Ejercicio 7

Num1 = int(input("Ingrese un número distinto de 0 porfavor"))
Num2 = int(input("Ingrese otro número distinto de 0 porfavor"))

Suma = Num1 + Num2
Resta  = Num1 - Num2
Multiplicacion = Num1 * Num2
Division = Num1 // Num2

print(f"El resultado de la suma es: {Suma}, el resultado de la resta es: {Resta}, el resultado de la multiplicación es: {Multiplicacion} y el resultado de la division es: {Division}")

# Ejercicio 8 

Altura = float(input("Ingrese su altura porfavor"))
Peso = float(input("Ingrese su peso porfavor"))

IMC = Peso / (Altura ** 2)

print(f"Tu indice de masa corporal es {IMC}")

# Ejercicio 9 

Celsius = float(input("Ingrese su temperatura en grados Celsius para convertirlo a Fahrenheit"))
Fahrenheit = ((9/5) * Celsius) + 32

print(f"La temperatura transformado en Fahrenheit es de {Fahrenheit} ")

# Ejercicio 10

Num1 = float(input("Ingrese un número"))
Num2 = float(input("Ingrese un número"))
Num3 = float(input("Ingrese un número"))

Promedio = (Num1 + Num2 + Num3) / 3

print(f"El promedio de los 3 numeros es {Promedio}");