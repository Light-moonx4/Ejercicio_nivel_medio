horas=int(input("hora de llegada:"))

if 0 <=horas<=23:
    if 6<=horas<=11:
        print("horario de la mañana")
    elif  10<=horas<=17:
        print("horario de la tarde")
    elif 18<=horas<=22:
        print("horario de la noche")
    else:
        print("fuera de horario de atencion")  