print("----- Bienvenido al Sistema de Inventario Python ------")

producto = []
cantidad = []
precio = []

i = True

while i == True:

    x = int(input("Ingresa =>\n1--Crear Producto\n2--Buscar Producto\n3--Eliminar Producto\n4--Ver Productos\n5--Salir\nPara indicar al programa: "))

    if x == 1:

        apro = input("Ingresa nombre producto: ").capitalize()
        acan = int(input("Ingresa cantidad del producto: "))
        apre = int(input("Ingresa precio del producto: "))

        producto.append(apro)
        cantidad.append(acan)
        precio.append(apre)

        print("----- Producto almacenado Correctamente -----")

    elif x == 2:

        busPro = input("Ingresa producto a Buscar: ").capitalize()

        resultado = busPro in producto

        if resultado == True:

            print("----- Producto Encontrado -----")

            elemento = producto.index(busPro)

            print("Nombre del Producto: ",producto[elemento])
            print("Cantidad del Producto: ",cantidad[elemento])
            print("Precio del Producto: ", precio[elemento])

            print("----- Busqueda Finalizada -----")
            

        else:
            print("----- Producto No Encontrado -----")

            print("----- Busqueda Finalizada -----")

    elif x == 3:

        busPro = input("Ingresa producto a Eliminar: ").capitalize()

        resultado = busPro in producto

        if resultado == True:

            print("----- Producto Encontrado -----")

            elemento = producto.index(busPro)

            del producto[elemento]
            del cantidad[elemento]
            del precio[elemento]

            print("----- Producto Eliminado Correctamente -----")

        else:

            print("----- Producto No Encontrado -----")

    elif x == 4:

        print("----- Productos en Inventario -----")

        for i in producto:

            print(i)

    elif x == 5:

        print("----- Hasta Pronto -----")

        i = False



