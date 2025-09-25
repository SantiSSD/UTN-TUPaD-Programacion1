# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

suma_minimas = 0
suma_maximas = 0

dias = ["lunes", "martes", "miercoles", "jueves","viernes", "sabado", "domingo"]
matriz =[
    [23,30],  #lunes
    [12,23],  #martes
    [22,33],  #miercoles
    [12,22],  #jueves
    [2,12],   #viernes
    [11,12],  #sabado
    [13,14] ] #domingo


for semana in matriz:

    suma_minimas += semana[0]
    suma_maximas += semana[1]


promedio_maximas = suma_maximas // 7
promedio_minimas = suma_minimas // 7

print(f"Promedio de temperatura maxima: {promedio_maximas} y promedio de temperatura minima: {promedio_minimas}")


mayor_amplitud = -1


for i in range(7):
    min_dia = matriz[i][0]
    max_dia = matriz[i][1]

    amp = max_dia - min_dia

    if amp > mayor_amplitud:

        mayor_amplitud = amp
        indice_mayor = i


print(f"El dia con mayor amplitud registrado es: {dias[indice_mayor]}, con {mayor_amplitud}")

