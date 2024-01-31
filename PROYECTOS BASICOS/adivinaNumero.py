import random

def adivina_el_numero(x):

    print ("=========================")
    print ("Bienvenido al juego")
    print ("=========================")
    print ("Tu meta es adivinar el numero generado por la computadora.")

    numero_aletatorio = random.randint(1, x) #Numero aletario entre 1 y xs

    prediccion = 0

    while prediccion != numero_aletatorio:
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: ")) #Usurio ingresa un numero

        if prediccion < numero_aletatorio:
            print ("Intenta nuevamente, el numero es muy pequeño")

        elif prediccion > numero_aletatorio:
            print ("Intenta nuevamente, el numero es muy grande")

    print (f"Felicitaciones has adivinado {numero_aletatorio} correctamente!")


adivina_el_numero(10)