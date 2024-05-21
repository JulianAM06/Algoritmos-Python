claveNueva = []
validarClave = []

print("Bienvenido al Sistema de Seguridad")
print("Vamos a Crear la Clave de Seguridad")

j = 0

while j < 4:

        x = int(input("Ingresa tu clave de 4 digitos, con numeros entre el 0 y 9: "))

        if x >= 0 and x <= 9:

            claveNueva.append(x)

            j = j + 1

        else:
            print("Recuerda usar un numero entre 0 y 9")
            
print("Clave Guardada Exitosamente")

print("Bienvenido al Sistema de chequeo")

print("Ingresa Clave de Seguridad")

i = True

while i == True:

    k = 0

    while k < 4:

        z = int(input("Ingresa digito: "))

        if x >= 0 and x <= 9:

            validarClave.append(z)

            k = k + 1

    if claveNueva[:] != validarClave[:]: 

            print("Acceso Denegado")

            validarClave.clear()

            i = True

    else:

        print("Acceso Permitido")

        i = False




        



