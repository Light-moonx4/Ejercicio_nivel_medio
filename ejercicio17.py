clientes = 1

total_dia = 0

corte = 0
cepillado = 0
tintura = 0

while clientes <= 7:

    print("\nCliente", clientes)

    nombre = input("Ingrese nombre: ")
    servicio = input("Ingrese servicio (corte, cepillado, tintura): ")
    valor = int(input("Ingrese valor pagado: "))

    total_dia = total_dia + valor

    if servicio == "corte":
        corte = corte + 1
    elif servicio == "cepillado":
        cepillado = cepillado + 1
    elif servicio == "tintura":
        tintura = tintura + 1

    clientes = clientes + 1


print("\n=== RESULTADOS ===")
print("Total del dia:", total_dia)
print("Cantidad de cortes:", corte)
print("Cantidad de cepillados:", cepillado)
print("Cantidad de tinturas:", tintura)

if corte > cepillado and corte > tintura:
    print("El servicio mas solicitado fue: corte")
elif cepillado > corte and cepillado > tintura:
    print("El servicio mas solicitado fue: cepillado")
else:
    print("El servicio mas solicitado fue: tintura")