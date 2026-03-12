horas=int(input("digite la cantidad de horas que estuvo parquiado:"))
pago_primera_hora=5000
pago_horas_extra=3000
if horas>0:
    if horas ==1:
        print("total a pagar:",pago_primera_hora)
    else:
        if horas !=1:
            horas-=1
            pago_horas_extra=pago_horas_extra*horas
            total=pago_primera_hora+pago_horas_extra
            print("total a pagar es:",total)
else:
    print("no parquino ni un hora")
    total=0
    print("total a pagar es",total)