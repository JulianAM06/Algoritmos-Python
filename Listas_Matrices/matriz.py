# EJERCICIO 1

fila = 3 # Cantidad de Filas en la Matriz - Alumnos
columna = 3 # Cantidad de Columnas en la Matriz - Notas

matrix = []

for posicion_fila in range(fila): # Ciclo para recorrer las Notas por cada Alumno
    fila = []
    for elemento in range(columna):
        fila.append(float(input(f"Ingresa nota al Alumno {posicion_fila}: ")))
    matrix.append(fila)
    
for fila in matrix: # Ciclo para mostrar las Notas en la Matriz
    for elemento in fila:
        print(elemento, end="  ")
    print() 
    
suma_notas = [] # Lista Vacia

for i in matrix: # Ciclo para recorrer todas las notas de cada alumno, sacar el promedio y almacenar el resultado en la lista vacia
    suma_notas.append(sum(i)/columna)
    
AG = 0 # Variable de Alumnos Ganadores, se inicia en 0
AP = 0 # Variable de Alumnos Perdedores, se inicia en 0

for j in suma_notas: # Ciclo para validar cada promedio y a su vez almacenar cada dato en un contador
    if j >= 3:
        AG = AG + 1
        print("Nota del Promedio Ganador", j)
    elif j < 3:
        AP = AP + 1

print("Cantidad de Alumnos Ganadores: ",AG)
print("Cantidad de Alumnos con Derecho a Recuperacion: ",AP)