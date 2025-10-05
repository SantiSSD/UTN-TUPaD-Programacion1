def reasignar_lista(lista):
    print("Dentro de la funcion antes de reasignar", lista)
    lista = [1,2,3,4]
    print("Dentro de la funcion despues de reasignar", lista)

mi_lista = [1,2,3]
reasignar_lista(mi_lista)

print("Lista fuera de la funcion", mi_lista)