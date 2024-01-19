import math
sum_min = 0
while True:
    min =int(input("Duracion tramo: "))
    sum_min += min
    if min == 0:
        t_hours = sum_min/60
        rest = sum_min%60
        parte_decimal,parte_entera = math.modf(t_hours)
        if rest < 10:
            print(f"Tiempo total del viaje: {int(parte_entera)}:0{rest} horas")
        else:
            print(f"Tiempo total del viaje: {int(parte_entera)}:{rest} horas")
            