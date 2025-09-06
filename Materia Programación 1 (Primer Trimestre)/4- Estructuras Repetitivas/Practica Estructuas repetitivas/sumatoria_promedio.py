cant_numeros = 5
sumatoria = 0
for cont in range(1, cant_numeros + 1):
    print("Ingrese un numero", cont)
    num = int(input())
    sumatoria = sumatoria + num

promedio = sumatoria / cant_numeros
print(f"El promedio es {promedio} ")