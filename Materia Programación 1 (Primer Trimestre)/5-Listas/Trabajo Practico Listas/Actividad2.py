# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for producto in range(5):
    producto = input(f"Ingrese el producto número {producto +1 }")
    productos.append(producto)

print("Lista Desordenada")
for i in range (len(productos)):
    print(f"El producto numero {i + 1} = {productos[i]}")

lista_ordenada = sorted(productos)

print("Lista Ordenada")

for i in range(len(lista_ordenada)):
    print(f"El producto numero {i + 1} = {lista_ordenada[i]}")

producto_eliminar = input("Ingrese el nombre del producto que desea eliminar")
producto_eliminar
if producto_eliminar in productos:
    productos.remove(producto_eliminar)

    print("Lista Actualizada de productos")

    for producto in productos:
        print(producto)

else:
    print(f"No se encontro el producto...")

