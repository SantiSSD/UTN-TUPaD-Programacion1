# Actividad 8

nombre = input("Ingrese su nombre por favor")
print("Ingrese el numero 1 si desea convertir su nombre en mayúsculas")

print("Ingrese el numero 2 si desea convertir su nombre en minúsculas")

print("Ingrese el numero 3 si desea convertir la primer letra de su nombre en mayúsculas")

numero = int(input("Ingrese el número:"))

if numero == 1:
    print(nombre.upper())

elif numero == 2:
    print(nombre.lower())

elif numero == 3:
    print(nombre.title())
else:
    print("Ingrese uno de los números solicitados por favor")
    

