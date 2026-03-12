cono=3000
vaso=4000
banana_split=9000
registro=0
productos1=0
productos2=0
productos3=0
continuar="y"
while continuar=="y":
    producto = input("digite el producto que decesa (cono , vaso ,banana_split):")
    cantidad= int(input("digite la cantidad que desea del producto:"))
    
    if producto=="cono":
        total=cono*cantidad
        productos1+=cantidad
    elif producto=="vaso":
        total=vaso*cantidad
        productos2+=cantidad
    elif producto=="banana_split":
        total=banana_split*cantidad
        productos3+=cantidad
    else:
        print("el producto no existe")
        total=0
    
    registro+=1
    total_vendido=total
    continuar=input("digite siguiente cliente o finalizar(y,n)")
    
if  productos1 > productos2 and productos1 > productos3:
    producto_mas_vendido ="cono"
elif productos2 > productos1 and productos2 > productos3:
    producto_mas_vendido ="vaso"
else:
    producto_mas_vendido = "banana_split"
       
        
print("cantida vendida:",total)
print("cantidad de clientes atendidos es:",registro)
print("el producto mas vendido es :",producto_mas_vendido)