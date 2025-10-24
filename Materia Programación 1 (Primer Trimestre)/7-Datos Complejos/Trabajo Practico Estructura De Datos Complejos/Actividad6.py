alumnos = []
notas = []
contador = 0
cant_notas = 0

while contador < 3:
    alumno = input("Ingresa el nombre de un alumno")
    
    for i in range(3):
        nota = int(input(f"Ingresa la nota numero {i + 1} "))
        notas.append(nota)
    tupla_notas = tuple(notas)

    alumnos.append((alumno,tupla_notas))
    contador += 1

print("Promedio De Los Alumnos")
for alumno, notas in alumnos:
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: promedio = {promedio}" )