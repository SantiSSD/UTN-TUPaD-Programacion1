# Actividad 5
Contra = input("Introduzca su contraseña de entre 8 y 14 caracteres ")

if len(Contra) > 7 and (len(Contra) < 15):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")