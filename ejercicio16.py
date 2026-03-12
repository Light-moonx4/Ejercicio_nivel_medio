ventas = 1

alimento = 0
juguete = 0
accesorio = 0

while ventas <= 10:

    print("\nVenta", ventas)

    categoria = input("Ingrese categoria (alimento, juguete, accesorio): ")
    valor = int(input("Ingrese valor de la compra: "))

    if categoria == "alimento":
        alimento = alimento + valor
    elif categoria == "juguete":
        juguete = juguete + valor
    elif categoria == "accesorio":
        accesorio = accesorio + valor

    ventas = ventas + 1


print("\n=== RESULTADOS ===")
print("Total vendido en alimento:", alimento)
print("Total vendido en juguete:", juguete)
print("Total vendido en accesorio:", accesorio)

if alimento > juguete and alimento > accesorio:
    print("La categoria que genero mas dinero fue: alimento")
elif juguete > alimento and juguete > accesorio:
    print("La categoria que genero mas dinero fue: juguete")
else:
    print("La categoria que genero mas dinero fue: accesorio")