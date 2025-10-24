agenda = {}

contador = 0

while contador < 4:
    dia = input("Ingresa el dia")
    hora = input("Ingresa el horario")
    evento = input("Ingresa el evento")

    clave = (dia,hora)

    agenda[clave] = evento
    contador += 1

consulta_dia = input("Que dia quisieras consultar?")
consulta_hora = input("Que hora quisieras consultar?")

consulta_clave = (consulta_dia, consulta_hora)

if consulta_clave in agenda:
    print(f"En ese horario hay {agenda[consulta_clave] } ")
else:
    print("No hay eventos en ese horario o dia")
