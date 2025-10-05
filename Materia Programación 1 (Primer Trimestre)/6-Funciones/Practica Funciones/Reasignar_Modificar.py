def reasignar(lista):
    lista = [100,200,300] #se crea una nueva lista y lista apunta a ella
    print(f"Dento de la funcion {lista}")

#Fuera de la función
nums = [1,2,3]
reasignar(nums)
print(f"fuera de la lista", nums)