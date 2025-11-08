def potencia_recursiva(numero, exponente):
    if exponente == 0:
        return 1
    else:
        return numero * potencia_recursiva(numero, exponente - 1)
    

numero = int(input("Ingrese un numero: "))
exponente = int(input("Ingresa el exponente del numero: "))

print(f" {numero} elevado a {exponente} es {potencia_recursiva(numero,exponente)}")

