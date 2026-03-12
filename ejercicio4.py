edad =int(input("digite su edad:"))
if edad<12:
    total_pagar=8000
    print("precio de entra es de:",total_pagar)
elif 12<=edad<=59:
    total_pagar=12000
    print("precio de entra es de:",total_pagar)
elif edad>60:
    total_pagar=9000
    print("precio de entra es de:",total_pagar)
else:
    print("invalido digite el numero de su edad")