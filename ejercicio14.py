capacidad = int(input("Ingrese la capacidad total de la sala: "))

personas = 0
ninos = 0
adultos = 0
adultos_mayores = 0

while personas < capacidad:

    print("\nRegistro de persona", personas + 1)

    edad = int(input("Ingrese la edad: "))

    if edad < 18:
        print("Clasificacion: Niño")
        ninos = ninos + 1
    elif edad < 60:
        print("Clasificacion: Adulto")
        adultos = adultos + 1
    else:
        print("Clasificacion: Adulto mayor")
        adultos_mayores = adultos_mayores + 1

    personas = personas + 1

print("\n=== RESULTADOS ===")
print("Total de personas ingresadas:", personas)
print("Niños:", ninos)
print("Adultos:", adultos)
print("Adultos mayores:", adultos_mayores)

if personas == capacidad:
    print("La sala se lleno")
else:
    print("La sala no se lleno")