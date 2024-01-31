def es_multiplo(numero1, numero2):
    # Si el residuo es 0, es multiplo
    if numero1 % numero2 == 0:
        return True
    else:
        return False
    

num1 = int(input("Digite el primer numero:"))
num2 = int(input("Digite el segundo numero:"))

print(es_multiplo(num1,num2))