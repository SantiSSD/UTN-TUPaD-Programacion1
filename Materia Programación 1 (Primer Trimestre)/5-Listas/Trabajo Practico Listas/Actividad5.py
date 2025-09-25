# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

estudiantes_presentes = ["Santiago", "Rodrigo", "Emanuel", "Benjamin", "Gonzalo","Carlos","Tomas","Marcos",]

print("Estudiantes Actuales")
for i in estudiantes_presentes:
    print(i, end=" ")
print("\nDesea agregar un nuevo estudiante?")
decision = input("Presione 1 si desea agregar un estudiante\nPresione 2 si desea eliminar un estudiante")
if decision != "1" and decision != "2":
    print("Ingreso un numero invalido...")
if decision == "1":
    agregar= input("Ingrese el nombre del estudiante que desea agregar")
    estudiantes_presentes.append(agregar)
    for lista in estudiantes_presentes:
        print(lista, end=" ")
if decision == "2":
    eliminar= input("Ingrese el nombre del estudiante que desea eliminar")
    if eliminar in estudiantes_presentes:
        estudiantes_presentes.remove(eliminar)
        for lista in estudiantes_presentes:
            print(lista, end=" ")
    else:
        print("No se encontro el estudiante...")
    