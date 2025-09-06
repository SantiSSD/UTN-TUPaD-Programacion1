Edad_Minima = 18
cantMayor = 0
cant_personas = int(input("Ingrese una cantidad de personas por favor"))
for cont in range(1, cant_personas + 1):
    print(f"ingrese la edad num° {cont}")
    Edad =int(input())
    if Edad >= Edad_Minima:
        cantMayor += 1

Porcentaje_Mayor = (cant_personas / cantMayor) * 100
print(f"El porcentaje de personas mayores de edad es {Porcentaje_Mayor}")