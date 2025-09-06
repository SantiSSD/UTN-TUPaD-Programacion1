corte = "*"
edad_minima = float("inf")
edad_maxima = float("-inf")
NOMBRE_INVALIDO = "XXXXXXXXXXXXX"
nombre_masjoven = NOMBRE_INVALIDO
edad = 0
nombre= input(f"Ingrese un nombre porfavor, utilice el caracter {corte} para cortar")
while nombre != corte:
    edad = int(input("Ingrese la edad de la persona por favor"))
    # PROCESO
    if edad < edad_minima:
        edad_minima = edad
        nombre_masjoven = nombre
    nombre= input(f"Ingrese otro nombre porfavor, utilice el caracter {corte} para cortar")

if nombre_masjoven == NOMBRE_INVALIDO:
    print("No ingresaron personas.... ")
else:
    print(f"la persona mas joven es {nombre_masjoven} con {edad_minima} años")
