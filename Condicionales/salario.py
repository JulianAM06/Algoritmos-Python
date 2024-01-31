S = float(input("Ingrese salario actual: "))

if S < 18000:
    
    NS = (S *0.12) + S
    
elif S >= 18000 or S <= 30000:
    
    NS = (S * 0.08) + S
    
elif S > 30000 or S <= 50000:
    
    NS = (S * 0.07) + S
    
else: 
    
    NS = (S * 0.06) + S
    
print("Su nuevo Salario es: ", NS)
    