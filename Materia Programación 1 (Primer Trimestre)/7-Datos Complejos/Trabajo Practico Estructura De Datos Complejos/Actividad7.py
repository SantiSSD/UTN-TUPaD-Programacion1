parcial_1 = {"Santiago","Tomas","Gonzalo","Lautaro"}
parcial_2 = {"Tomas","Santiago", "sofia","evelyn"}
ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
almenos_uno = parcial_1 | parcial_2
print(f"Aprobaron ambos parciales {ambos}")

print(f"Los que aprobaron solo un parcial = {solo_uno}")

print(f"Los que aprobaron almenos un parcial {almenos_uno}")
