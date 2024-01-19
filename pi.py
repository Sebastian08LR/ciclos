num = int(input('Ingrese un numero entero para determinar la suma: '))
sum=0
for i in range(num):
    sum+=(-1)**(i)*(1/(2*i+1))
out_pi = 4 * sum
print(out_pi)