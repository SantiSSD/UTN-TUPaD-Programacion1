def repetir_frase(num,frase):
    if num >= 1:
        print(frase)
        repetir_frase(num - 1, frase )

repetir_frase(5, "pepe")