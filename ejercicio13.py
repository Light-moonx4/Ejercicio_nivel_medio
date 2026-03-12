total_dia = 0
producto = ""

print("=== CAFETERIA ===")

while producto != "salir":

    total_cliente = 0
    producto = input("\nIngrese producto (cafe, capuchino, pastel) o 'salir': ")

    while producto != "salir":

        if producto == "cafe":
            precio = 4000
        elif producto == "capuchino":
            precio = 7000
        elif producto == "pastel":
            precio = 6000
        else:
            print("Producto no valido")
            producto = input("Ingrese producto (cafe, capuchino, pastel) o 'salir': ")
            continue

        total_cliente = total_cliente + precio
        print("Total parcial:", total_cliente)

        producto = input("Ingrese otro producto o 'salir': ")

    if total_cliente > 20000:
        descuento = total_cliente * 0.10
        total_cliente = total_cliente - descuento
        print("Se aplico 10% de descuento")

    if total_cliente > 0:
        print("Total a pagar por el cliente:", total_cliente)
        total_dia = total_dia + total_cliente

print("\nTotal acumulado del dia:", total_dia)