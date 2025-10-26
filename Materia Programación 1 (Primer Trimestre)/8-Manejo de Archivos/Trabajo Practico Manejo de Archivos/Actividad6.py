lista_productos = []

with open("productos.txt", "r") as productos:
    lineas = productos.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        diccionario_productos = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        lista_productos.append(diccionario_productos)
    
nuevo_producto = {"nombre" : "mochilas", "precio" : "2200", "cantidad": "15"}

lista_productos.append(nuevo_producto)

with open("productos.txt", "w") as productos:
    for producto in lista_productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        productos.write(linea)

with open("productos.txt", "r") as productos:
    lineas = productos.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        print(f"Nombre: {nombre} | Precio: {precio} | Cantidad: {cantidad}\n ") 