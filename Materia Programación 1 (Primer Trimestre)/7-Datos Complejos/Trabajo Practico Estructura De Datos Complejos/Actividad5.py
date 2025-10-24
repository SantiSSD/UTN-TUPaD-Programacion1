frase = input("Ingrese una frase")
palabras = frase.split()
conjunto = set(palabras)

print(f"Palabras unicas {conjunto}")

recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"conteo palabras {recuento}")