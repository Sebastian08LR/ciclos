num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
sum = 0 
for i in range(num1+1, num2):
    sum += i
    
print(f"La suma de todos los numeros entre {num1} y {num2} es = {sum}")
