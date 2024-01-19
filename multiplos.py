num = int(input("Ingrese un numero entero: "))
dig_mult = 0

while dig_mult <= 10:
    mult = num * dig_mult
    print(f"{num} x {dig_mult} = {mult}")
    dig_mult += 1