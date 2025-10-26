# with open ("metodos.csv" , "w") as productos:
#     productos.write("Lapicera,200,30\n")
#     productos.write("Cuaderno,300,20\n")
#     productos.write("Gomas,500,20")

# lineas = [
#     "Nombre,Precio,Cantidad\n",
#     "Compas,200,12\n",
#     "Tijera,300,10\n"
# ]

# with open("metodos.csv", "w") as productos:
#     productos.writelines(lineas)

# print("Para lectura tenemos")

# with open ("metodos.csv", "r") as productos:
#     encabezado = productos.readline().strip()
#     print("Encabezado:", encabezado)
#     linea1 = productos.readline().strip()
#     print("Primera linea:", linea1 )
#     linea2 = productos.readline().strip()
#     print("Primera linea:", linea2 )

# print("También tenemos readlines()")

# with open("metodos.csv", "r") as productos:
#     lineas = productos.readlines()
#     for linea in lineas:
#         partes = linea.strip().split(",")
#         print(partes)

