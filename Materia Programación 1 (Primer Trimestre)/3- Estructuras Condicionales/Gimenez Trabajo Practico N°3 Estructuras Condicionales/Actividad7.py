# Actividad 7
frase = input("Ingrese una frase")
ultima_letra = frase[-1].lower()
vocal = "aeiou"

if ultima_letra in vocal:
    print(f"{frase}!")    
else:
    print(frase)