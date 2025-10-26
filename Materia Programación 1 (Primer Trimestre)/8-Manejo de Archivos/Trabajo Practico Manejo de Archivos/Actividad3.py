
with open("productos.txt", "a") as productos:
    print("Ingresa un nuevo producto")
    nombre = input("Ingresa el nombre del producto")
    precio = input("Ingresa el precio del producto")
    cantidad = input("Ingresa la cantidad del producto")

    productos.write(f"{nombre}, {precio}, {cantidad}")

    
print("Nuevo Producto Agregado")
with open("productos.txt", "r") as productos:
    lineas = productos.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]

        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")