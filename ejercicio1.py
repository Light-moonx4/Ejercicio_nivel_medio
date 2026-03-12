vainilla=0
chocolate=0
fresa=0

for i in range(0,5,1):
    helado= int(input("que saber de helado deseas 1.vainilla,2.chocolate,3.fresa:"))
    
    if helado == 1:
        vainilla += 1
    elif helado== 2:
        chocolate += 1
    elif helado== 3:
        fresa += 1
    else:
        print("sabor invalido favor de elegir un numero 1.vainilla,2.chocolate,3.fresa:")

print("numero de pedido por sabor:")
print("vainilla:",vainilla)
print("chocolate:",chocolate)
print("fresa:",fresa)