contactos = {}

contacto = 0
while contacto != 2:
    nombre = input("Ingrese el nombre del contacto")
    numero = input("Ingrese el numero del contacto")
    contactos[nombre] = numero
    contacto +=1

consulta = input("Ingrese el nombre de quien quisieras obtener su numero")

if consulta in contactos:
    print(f"El numero del nombre {consulta} es {contactos[consulta]}")
    
else:
    print("El nombre ingresado no existe en la agenda de contactos")
