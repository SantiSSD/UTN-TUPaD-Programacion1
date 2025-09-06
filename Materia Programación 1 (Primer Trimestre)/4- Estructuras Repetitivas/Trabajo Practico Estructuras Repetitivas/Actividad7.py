numero1 = 0
suma = 0
numero2 = int(input("Ingrese un numero positivo"))

for i in range(numero1 + 1, numero2):
    
    suma += i

print(f"La suma de todos los números comprendidos entre 0 y {numero2} es {suma}")