# Actividad 9
magnitud = float(input("Ingrese la magnitud de un terremoto, según la escala de richter"))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)") 
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños.)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles.)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte (puede causar daños significativos.)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala.)")

