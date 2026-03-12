personas = 1

bajo = 0
medio = 0
alto = 0

while personas <= 5:
    print("\nRegistro de la persona", personas)

    nombre = input("Ingrese el nombre: ")
    dias = int(input("Ingrese los dias asistidos en la semana: "))
    minutos = int(input("Ingrese minutos promedio entrenados por dia: "))

    if dias < 3:
        print(nombre, "tiene bajo compromiso")
        bajo = bajo + 1
    elif dias >= 3 and dias <= 4:
        print(nombre, "tiene compromiso medio")
        medio = medio + 1
    else:
        print(nombre, "tiene compromiso alto")
        alto = alto + 1

    personas = personas + 1

print("\nResultados finales")
print("Personas con bajo compromiso:", bajo)
print("Personas con compromiso medio:", medio)
print("Personas con compromiso alto:", alto)