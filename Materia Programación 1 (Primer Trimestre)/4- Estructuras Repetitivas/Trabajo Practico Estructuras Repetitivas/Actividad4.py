numero = -1
suma = 0

while numero != 0:
    numero = int(input("Ingrese un numero entero por favor, presione 0 si desea finalizar el ciclo"))
    suma += numero
   
if suma == 0:
    print(f"no se sumo ningún número la suma queda como {suma} ")
else:
    print(f"La suma de todos los numeros es de {suma}")