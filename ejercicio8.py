productos=0
while productos==0:
    producto1=int(input("digita el precio del balon de futbol:"))
    producto2=int(input("digita el precio de guantes de boxeo:"))
    producto3=int(input("digita el precio de el bate de beisboll:"))
    producto4=int(input("digita el precio de la pelota de golf:"))
    producto5=int(input("digita el precio de la raqueta de tenis:"))
    producto6=int(input("digita el precio de cuerda de ginasio:"))
    if producto1 >100000:
        productos+=1
    if producto2>100000:
        productos+=1
    if producto3>100000:
        productos+=1
    if producto4>100000:
        productos+=1
    if producto5>100000:
        productos+=1
    if producto6>100000:
        productos+=1

    if productos == 0:
        print("No hay productos que superen los 100000")


print("la cantidad de productos deportivos que cuestan mas de 100000 de los seis es:",productos)