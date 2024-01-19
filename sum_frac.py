frac=1
count = 1
sum=0
#hace print del cabecero para organizar la salida de los datos en las columnas
title = ['POTENCIA', 'FRACCIÓN', 'SUMA']
for t in title:
    print(t, end=' ')
print()

while frac>0.000001:
    frac=1/(2**count)
    sum+=frac
    print(str(count).ljust(8), end=' ')
    print(str(round(frac,4)).ljust(8), end=' ')
    print(round(sum,4))
    count+=1