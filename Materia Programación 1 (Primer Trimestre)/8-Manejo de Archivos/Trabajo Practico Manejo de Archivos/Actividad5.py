nombre_producto = input("Ingresa el nombre del producto que desea buscar")
lista_productos = []
with open("productos.txt", "r") as productos:
    lineas = productos.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]

        diccionario_produtos = {
            "nombre" : nombre,
            "precio" : precio,
            "cantidad": cantidad
        }
        lista_productos.append(diccionario_produtos)

for producto in lista_productos:
    if producto["nombre"].lower() == nombre_producto.lower():
        print("Producto Encontrado")
        print(f"Nombre del producto {producto['nombre']}")
        print(f"Precio del producto {producto['precio']}")
        print(f"Cantidad del producto {producto['cantidad']}")
        break
    else:
        print("No se encontro el producto...")
        break