import random

numeroSecreto = random.randint(1, 5)

comprobar = True

while comprobar == True:

    x = int (input("Bienvenido al juego Adivina Numero, Ingresa numero a Adivinar entre 1 y 5: "))

    if x == numeroSecreto:
    
        comprobar = False
        print("Adivinaste el numero")
        
    else:
        print("Muy malo sigue intentando!!!")
    
    
