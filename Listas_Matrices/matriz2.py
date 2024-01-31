# EJERCICIO 2

matriz =[
    [35, 41, 70, 85],
    [12, 46, 87, 10],
    [6, 30, 29, 95],
    [15, 78, 55, 40]
]

numero_mayor = []

for j in matriz:
    numero_mayor.append(max(j))

print("Numeros Mayores de cada Fil: ",numero_mayor)

suma_numeros_filas = []

for i in matriz:
    suma_numeros_filas.append(sum(i))
    
print("Suma de cada Fila: ",suma_numeros_filas)