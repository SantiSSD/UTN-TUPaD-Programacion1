paises_a_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París"
}

invertido = {}
for pais, capital in paises_a_capitales.items():

    invertido[capital] = pais
    
print(f"Diccionario Original {paises_a_capitales}")
print(f"Diccionario Invertido {invertido}")