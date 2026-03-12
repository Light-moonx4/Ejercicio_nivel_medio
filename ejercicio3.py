cafe=4000
te=3500
jugo=5000
print("bienvenido que bebida deseas(1.cafe-4000 , 2.te-3500 ,3.jugo-5000)")
bebida= int(input("que bebida deseas :"))
if bebida== 1 or bebida==2 or bebida==3:
    cantidad=int(input("cuantas bebidas deseas:"))
    if bebida == 1:
        total_pagar = cafe*cantidad
    elif bebida == 2:
        total_pagar = te*cantidad
    elif bebida == 3:
        total_pagar = jugo*cantidad
else:
    print("opcion invalida")
    bebida= int(input("que bebida deseas digite porfavor (1 para cafe , 2 para te , 3 para jugo):"))
 
if bebida!=1 or bebida !=2 or bebida!=3:
    print("programa finalizado")
    total_pagar=0
print("total a pagar es:",total_pagar)
