productos = {"hamburguesa": 5, "Coca-Cola": 2, "Cerveza" : 5 }

producto = input("Ingresa el nombre de un producto")

if producto in productos:
    stock = int(input(f"Agrega el stock del producto {producto}"))
    productos[producto] += stock
else:
    print("El producto no existe se agregara uno nuevo")
    stock = int(input(f"Agrega el stock del nuevo producto {producto}"))
    
    productos[producto] = stock 

print(f"Productos actualizados = {productos}")