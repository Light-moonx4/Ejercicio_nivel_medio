productos = 1

agotado = 0
stock_bajo = 0
stock_normal = 0

while productos <= 10:

    print("\nProducto", productos)

    nombre = input("Ingrese nombre del producto: ")
    cantidad = int(input("Ingrese cantidad disponible: "))

    if cantidad == 0:
        print("Estado: Agotado")
        agotado = agotado + 1
    elif cantidad <= 5:
        print("Estado: Stock bajo")
        stock_bajo = stock_bajo + 1
    else:
        print("Estado: Stock normal")
        stock_normal = stock_normal + 1

    productos = productos + 1


print("\n=== RESULTADOS ===")
print("Productos agotados:", agotado)
print("Productos con stock bajo:", stock_bajo)
print("Productos con stock normal:", stock_normal)