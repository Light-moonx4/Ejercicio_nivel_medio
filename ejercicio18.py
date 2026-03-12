estudiantes = 1
cantidad = int(input("Ingrese cantidad de estudiantes: "))

bajo = 0
medio = 0
alto = 0

suma_promedios = 0

mejor_promedio = 0
mejor_estudiante = ""

while estudiantes <= cantidad:

    print("\nEstudiante", estudiantes)

    nombre = input("Ingrese nombre: ")
    speaking = float(input("Nota speaking: "))
    listening = float(input("Nota listening: "))
    reading = float(input("Nota reading: "))

    promedio = (speaking + listening + reading) / 3
    print("Promedio:", promedio)

    suma_promedios = suma_promedios + promedio

    if promedio < 60:
        bajo = bajo + 1
    elif promedio < 80:
        medio = medio + 1
    else:
        alto = alto + 1

    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

    estudiantes = estudiantes + 1


promedio_general = suma_promedios / cantidad

print("\n=== RESULTADOS ===")
print("Promedio general del grupo:", promedio_general)
print("Mejor estudiante:", mejor_estudiante)
print("Mejor promedio:", mejor_promedio)

print("Nivel bajo:", bajo)
print("Nivel medio:", medio)
print("Nivel alto:", alto)