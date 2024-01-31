n = int (input("Ingrese el numero de acuerdo al siguiente menu:\nSegundos--1\nMinutos--2\nHoras--3\nPara saber el formato a operar: "))
x = float(input("Ingrese el valor: "))

RM = 0
RS = 0
RH = 0

if n ==1:
        RS = x
        RM = x * 0.0166667
        RH = x * 0.000277778
        
elif n ==2:
        RS = x * 60
        RM = x
        RH = x * 0.0166667

elif n ==3:
        RS = x * 3600
        RM = x * 60
        RH = x
    
    
 
print("En Segundos es: ",RS)
print("En Minutos es: ",RM) 
print("En Horas es: ",RH)