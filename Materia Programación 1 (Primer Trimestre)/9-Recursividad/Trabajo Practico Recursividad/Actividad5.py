def es_polindromo(palabra):
    if len(palabra) <= True:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_polindromo(palabra[1: -1])


texto = input("Ingrese un texto para verificar si es palindromo: ")

print(es_polindromo(texto))