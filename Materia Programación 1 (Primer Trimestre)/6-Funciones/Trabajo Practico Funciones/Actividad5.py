#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

def segundos_a_horas(segundos):
     minutos = segundos // 60
     horas = minutos // 60
     
     return horas

segundos = int(input("Ingresa una cantidad de segundos para convertilos a horas: "))

horas  = segundos_a_horas(segundos)


print(f"Los segundos transformados en horas son {horas} horas")