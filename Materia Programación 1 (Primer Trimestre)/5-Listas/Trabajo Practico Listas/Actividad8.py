# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 
estudiantes = ["pedro", "gonzalo", "armani", "franco", "pepe"]
materias = ["Matemáticas", "Lengua", "Programación"]
notas = [
    [8,7,8],  #pedro
    [5,2,8],  #gonzalo
    [10,7,10], #armani
    [7,7,2],  #franco
    [6,1,8],  #pepe
         ]


print("Notas   (fila = estudiantes, columnas = materias):")

for i in range (len(estudiantes)):
    print(f"Estudiante: {estudiantes[i]}, Notas: {notas[i]} ")

print("Promedio Por Estudiante")
for i in range(len(estudiantes)):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    
    promedio = suma // 3
    print(f" {estudiantes[i]} : {promedio}")


print("Promedio Materia")

for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    promedio = suma // 5
    print(f" {materias[j]} : {promedio}")

    