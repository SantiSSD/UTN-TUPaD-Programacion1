# Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
 [5,4,3,2,5,6,12], #Producto 1
 [2,4,4,2,1,6,7], #Producto 2
 [5,4,3,1,5,6,1], #Producto 3
 [5,4,3,1,5,6,7]  #Producto 4
 ]

totales_productos = []

for productos in range(0,4):
    total_producto = 0
    for dias in range(0,7):
        total_producto += ventas[productos][dias]
            
    totales_productos.append(total_producto)
    print(f"Producto{productos + 1} : {total_producto}")

#Dia con Mayores ventas
dia_maxventas = 0
dia_mayor = 0
for dia in range(0,7):
    total_dia = 0
    for producto in range(0,4):
        total_dia += ventas[producto][dia]
    print(f"Total del dia {dia + 1} : {total_dia}")
    if total_dia > dia_maxventas:
        dia_maxventas = total_dia
        dia_mayor = dia
print(f"el dia que mas se vendio fue el dia {dia_mayor + 1} con {dia_maxventas} ventas")


#Producto mas vendido de la semana

mayor_producto = 0
indice_producto = 0
for productos in range(0,4):
    if totales_productos[productos] > mayor_producto:
        mayor_producto = totales_productos[productos]    
        indice_producto = productos
print(f"El producto mas vendido de la semana fue el producto {indice_producto +1} con un maximo de {mayor_producto} ventas")