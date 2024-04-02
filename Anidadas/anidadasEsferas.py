esfera1 = int(input("Ingresa primer valor: "))
esfera2 = int(input("Ingresa segundo valor: "))
esfera3 = int(input("Ingresa tercer valor: "))

if esfera1 % 2 == 0 and esfera2 == esfera3:

    print("Esferas Correctas")

elif esfera2 % 2 == 0 and esfera1 == esfera3:

    print("Esferas Correctas")

elif esfera3 % 2 == 0 and esfera1 == esfera2:

    print("Esferas Correctas")

else:

    print("Esferas Incorrectas")