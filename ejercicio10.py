cantidad_asistencia = int(input("digite la cantidad de asistencia:"))

if cantidad_asistencia<5:
    print("asistencia baja")
    print("rango bajo")
elif 5<=cantidad_asistencia<=8:
    print("asistencia media")
    print("rango medio")
elif cantidad_asistencia>=9:
    print("asistencia alta")
    print("rango alto")