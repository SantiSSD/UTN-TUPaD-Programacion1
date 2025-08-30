# Actividad 6
from statistics import mode, median , mean
import random

numero_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numero_aleatorios)
mediana = median(numero_aleatorios)
mod = mode(numero_aleatorios)

if media > mediana and mediana > mod:
    print(f"Hay sesgo positivo {media} > {mediana} > {mod}")
elif media < mediana and mediana < mod:
    print(f"Hay sesgo negativo {media} < {mediana} < {mod}")
elif media == mediana and mediana == mod:
    print("Sin sesgo")
else:
    print("No se puede determinar con certeza")


