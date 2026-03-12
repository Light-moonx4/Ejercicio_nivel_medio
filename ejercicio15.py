vehiculos = 1

total_recaudado = 0
carros = 0
motos = 0

mayor_pago = 0
placa_mayor = ""

while vehiculos <= 8:

    print("\nRegistro del vehiculo", vehiculos)

    placa = input("Ingrese la placa: ")
    tipo = input("Ingrese tipo (carro/moto): ")
    horas = int(input("Ingrese horas parqueado: "))

    if tipo == "carro":
        pago = horas * 4000
        carros = carros + 1
    else:
        pago = horas * 2000
        motos = motos + 1

    print("Pago del vehiculo:", pago)

    total_recaudado = total_recaudado + pago

    if pago > mayor_pago:
        mayor_pago = pago
        placa_mayor = placa

    vehiculos = vehiculos + 1

print("\n=== RESULTADOS ===")
print("Total recaudado:", total_recaudado)
print("Cantidad de carros:", carros)
print("Cantidad de motos:", motos)
print("Vehiculo que pago mas:", placa_mayor)
print("Valor pagado:", mayor_pago)