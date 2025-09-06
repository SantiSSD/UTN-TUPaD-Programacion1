cant_numeros = 4
maximo = float("-inf")
minimo = float("inf")
pos_max = -1
pos_min = -1
for cont in range(1, cant_numeros + 1):
    print ("Ingrese un número"), (cont )
    num = int(input())
    

    if num > maximo:
        maximo = num
        pos_max = cont
    if num < minimo:
        
        minimo = num 
        pos_min = cont


print(f"el minimo es {minimo} y salio en la posicíon  {pos_min} ") 
print(f"el maximo es {maximo} y salio en la posición {pos_max}") 

