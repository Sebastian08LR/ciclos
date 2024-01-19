num = int(input("Ingrese el numero del cual desea sacar las potencias: "))
cant_pot = int(input("Ingrese la cantidad de potencias que desea sacar: "))
potencias = list()
for i in range(cant_pot):
    potencia = num**(i+1)
    potencias.append(potencia)

print(f"\n\t {potencias}")
    