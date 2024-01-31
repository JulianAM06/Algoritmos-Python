def Fib(numero):
         if numero <=0:
                 return 0
         if numero  ==1 or numero ==2:
                 
                 return 1
         return Fib(numero-1) + Fib(numero-2)

numero = int(input("Hasta donde desea generar la secuencia de fibonacci:"))
print(f"El numero fibonacci para {numero}, es {Fib(numero)}")
    