
from traceback import print_tb


centinela1=100
centinela=0
i=None
print("Crea tu salpicón")
print()
salpicon=[]
fruta = {}
    
for centinela in range (2): 
    i=input("Ingresa el nombre de la fruta: ")
    fruta['nombre']=i
    i=input("Ingresa el color de la fruta: ")
    fruta['color']=i
    i=input("Ingresa el precio de la fruta: ")
    fruta['precio']=i

    print("La fruta se ha guardade exitosamente")

    salpicon.append(fruta)

else:
    salpicon.reverse()
    print(salpicon)
