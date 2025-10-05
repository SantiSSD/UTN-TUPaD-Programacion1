def operar_lista(lista):
    lista.append(10) #Modifica el objeto original
    lista = [0,0,0] # Reasigna la variable local
    print("Despues de reasignar", lista) 
lista = [1,2,3]
operar_lista(lista)
print("Lista final", lista)