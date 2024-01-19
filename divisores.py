numero = int(input("Ingrese un numero entero: "))
divisores = list([])
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)
        
print(f"Los divisores de {numero} son {divisores}")