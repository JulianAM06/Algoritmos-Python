miLista = ['julian', 'Gabriela', 'Matias', 'Marta', 'Oscar'] # Los indices inician desde la posicion 0

print(miLista[:]) # Imprimir toda la lista 

print(miLista[2]) # Imprimir elemento del indice 2

print(miLista[-2]) # Imprime elemento empezando desde el utlimo hacia atras

print(miLista[0:2]) # Imprime los elementos empezando desde el indice 0 sin incluir el 2, es decir 0 y 1

print(miLista[:3]) # Si no se pone el primer indice, el sitema toma el 0

print(miLista[3:]) # Imprime los dos ultimos elementos de la lista en este caso. Posicion 3 y 4

miLista.append('Rocio') # Para adicionar un nuevo elemento a la lista, se inserta en la ultima posicion 

print(miLista)

miLista.insert(3, 'Dora') # Para adicionar un nuevo elemento, pero indicando la posicion donde se va ubicar

print(miLista)

miLista.extend(['Omar','Maximiliano','Jorge']) # Para adicionar varios elementos al final de la lista

print(miLista)

print(miLista.index('Oscar')) # Para saber la poscion del elemento en la lista, si hay dos elementos iguales, devuelve la posicion del primero

print('Matias' in miLista) # Para consultar si un elemento se encuentra en una lista TRUE/FALSE

miLista.remove('Dora') # Para eliminar un elemento de la lista

print(miLista)

miLista.pop() # Para eliminar el ultimo elemento de la lista

print(miLista)

milista2 = [5, 7.26, 'Reynaldo']

milista3 = miLista + milista2 # Se pueden sumar dos listas y dejar una sola

print(milista3)

print(milista2 * 3) # Para repetir las veces que necesitemos la lista

milista3[10] = "Nidia" # Para modificar un elemento en especifico

print(milista3)

milista2.clear() # Para eliminar todos los elementos de una lista

print(milista2)

milista3.pop(0) # Para eliminar un elemento especifico por su posicion

print(milista3)