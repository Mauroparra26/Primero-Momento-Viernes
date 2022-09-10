eleccion= 0
j=None
p=None
x=None
productos=[]

while eleccion != 5:

    print("***SHOPPING***")
    print("***************")
    print("1. Agregar Producto")
    print("2. Mostrar productos registrados")
    print("3. Editar productos registrados")
    print("4. Eliminar productos registrados")
    print("5. SALIR")

    producto = {}

    eleccion= int(input('Digite la opcion del Menu: '))

    if eleccion == 1:


        codigo= input('Digite el codigo del producto: ')

        nombre = input('Digite el nombre del producto: ')

        precio = input('Digite el precio del producto: ')
               


        producto['codigo']= codigo

        producto['nombre'] = nombre

        producto['precio']= precio

        print('Producto guardado exitosamente')

        productos.append(producto)

    elif eleccion == 2:

        print(productos)

    elif eleccion== 3:
        j=input('Digite el codigo del producto a modificar: ')
        p=input('Digite nuevo valor del producto:')
        productos['codigo']=p
    elif eleccion==4:
        print("Digite una opcion correcta ")
else:
    print('Bye') 
