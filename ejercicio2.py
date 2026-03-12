edad =int(input("digite su edad:"))

if edad<13:
    print("no puede ingresar menor de 13")
elif 13<=edad<=17:
    print("clase juvenil")
elif 18<=edad<=59:
    print("clase general")
elif edad >=60:
    print("clase senior")
else:
    print("invalido digite el numero de su edad")