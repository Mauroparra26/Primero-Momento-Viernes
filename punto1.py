i=None
centinela=0
numeros={}
multiplos2=[]
multiplos3=[]
cantidad=int(input("Digite cuantos numeros desea ingresar "))
while(centinela!=cantidad):
    centinela=centinela+1
    i=int(input("Digite un número: "))

    if (i%2) == 0: 
      multiplos2.append(i)

    elif (i%3) == 0:
      multiplos3.append(i)
      
    numeros['multiplosde2']= multiplos2
    numeros['multiplosde3'] =multiplos3

else: 
    print(numeros) 