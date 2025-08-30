# Actividad 10
print("Ingrese en el hemisferio en el cual se encuentra N/S")
hemisferio = input().lower()

print("Ingrese en que mes del año se encuentra 1-12")
mes = int(input())

print("Ingrese que dia del año es 1-31")
dia = int(input())
estacion = ""

if hemisferio == "n":
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "invierno"
        print(estacion)

    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "primavera"
        print(estacion)

    elif (mes == 6 and dia >= 21) or (mes in[7,8]) or (mes == 9 and dia <=20):
        estacion = "verano"
        print(estacion)

    elif (mes == 9 and dia >=21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        estacion = "otoño"
        print(estacion)

    else:
        print("Fecha invalida")
elif hemisferio == "s":   
    if (mes == 12 and dia >= 21) or (mes in [1,2]) or (mes == 3 and dia <= 20):
        estacion = "verano"
        print(estacion)

    elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
        estacion = "otoño"
        print(estacion)

    elif (mes == 6 and dia >= 21) or (mes in[7,8]) or (mes == 9 and dia <=20):
        estacion = "invierno"
        print(estacion)

    elif (mes == 9 and dia >=21) or (mes in [10,11]) or (mes == 12 and dia <=20):
        estacion = "primavera"
        print(estacion)
    else:
        print("Fecha invalida")
else:
    print("Hemisferio invalido")

