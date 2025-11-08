# Actividad Integradora: Gestor de Productos

# ===== Actividad 1: Crear archivo inicial con productos =====
# Este paso se hace manualmente: crear un archivo productos.txt con este contenido:
'''
Lapicera,120.5,30
Cuaderno,300.0,15
Goma,80.0,50
'''

# ===== Actividad 2: Leer y mostrar productos =====
def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# ===== Actividad 3: Agregar productos desde teclado =====
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad: ")
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado con éxito.\n")

# ===== Actividad 4: Cargar productos en una lista de diccionarios =====
def cargar_productos_en_lista():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

# ===== Actividad 5: Buscar producto por nombre =====
def buscar_producto(productos):
    nombre_buscado = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"Producto encontrado: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

# ===== Actividad 6: Guardar productos actualizados =====
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Archivo actualizado correctamente.\n")