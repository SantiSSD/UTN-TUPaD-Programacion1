# def modificar_valor(x):
#     print("Dentro de la funcion antes de reasignar", x)
#     x = 20
#     print("Dentro de la función despues de reasignar", x)

# a = 10

# modificar_valor(a)
# print("Fuera de la función", a)

def modificar_lista(lista):
    print("Dentro de la función antes de modificar", lista)
    lista.append(4)
    print("Dentro de la funcion despues de modificar", lista)


mi_lista= [1,2,3]
modificar_lista(mi_lista)
print("fuera de la funcion", mi_lista)
