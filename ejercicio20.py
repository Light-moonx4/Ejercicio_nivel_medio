personas = 1
cantidad = int(input("Ingrese cantidad de personas a registrar: "))

total_recaudado = 0

basico = 0
premium = 0
familiar = 0

while personas <= cantidad:

    print("\nPersona", personas)

    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    plan = input("Ingrese tipo de plan (basico, premium, familiar): ")

    if plan == "basico":
        pago = 50000
        basico = basico + 1
    elif plan == "premium":
        pago = 90000
        premium = premium + 1
    else:
        pago = 130000
        familiar = familiar + 1

    total_recaudado = total_recaudado + pago

    if edad < 18:
        print("Registro juvenil")
    elif edad >= 60:
        print("Beneficio senior")

    personas = personas + 1


print("\n=== RESULTADOS ===")
print("Total recaudado:", total_recaudado)

print("Personas con plan basico:", basico)
print("Personas con plan premium:", premium)
print("Personas con plan familiar:", familiar)

if basico > premium and basico > familiar:
    print("Plan mas vendido: basico")
elif premium > basico and premium > familiar:
    print("Plan mas vendido: premium")
else:
    print("Plan mas vendido: familiar")