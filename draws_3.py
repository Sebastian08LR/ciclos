
side = int(input("Ingrese el lado del hexágono: "))
longF = side + 2*(side-1)
#IMPRIME LA PARTE DE ARRIBA DEL HEXÁGONO
for i in range(side):
    crt=''
    for j in range(side+2*i):
        crt+='*'
    print(crt.center(longF))
    
#IMPRIME LA PARTE DE ABAJO DEL HEXÁGONO    
for x in range(1,side):
    crt=''
    for j in range(2,side+2*(side-x),1):
        crt +='*'
    print(crt.center(longF))