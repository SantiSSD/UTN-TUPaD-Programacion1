# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

notas = [1,3,6,5,0,3,10,8,9,10]

cantidad_notas = len(notas)

print(f"La cantidad de notas es: {cantidad_notas}" )

print("Notas cargadas:")
for i in(notas):

    print(i, end=" ")    

suma = 0

for i in (notas):

    suma += i

promedio = suma / cantidad_notas
menor = notas[0]
mayor = notas[0]
for nota in (notas):

    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota


print(f"\nEl promedio de las {cantidad_notas} notas es {promedio}")
print(f"La notas mas alta es {mayor} y la nota mas baja es {menor}")

