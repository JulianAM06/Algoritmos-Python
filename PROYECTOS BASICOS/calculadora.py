num1 = int (input("Ingresa el primer numero: "))
operador = input("Ingrese el operador \nSuma--(+)\nResta--(-)\nMultiplicacion--(*)\nDivision--(/)\nPara realizar la operacion: ")
num2 = int (input("Ingresa el segundo numero: "))

if operador =="+":
    R = num1 + num2

elif operador == "-":
    R = num1 - num2

elif operador == "*":
    R = num1 * num2

elif operador == "/":
    R = num1 / num2

print ("El resultado es: ",R)

