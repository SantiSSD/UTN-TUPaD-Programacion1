def contar_digitos_recursivo(num, digito):
    if num < 10:
        if num == digito:
            return 1
        else:
            return 0
    
    ultimo_digito = num % 10
    numero_sin_ultimo_digito = num // 10

    if ultimo_digito == digito:
        return 1 + contar_digitos_recursivo(numero_sin_ultimo_digito, digito)
    else:
        return contar_digitos_recursivo(numero_sin_ultimo_digito, digito)
    

print(contar_digitos_recursivo(1233, 3 ))