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

otraLista =[1,2,3,4,5,6,7,8,9,10]

otraLista.reverse() # Para revertir del ultimo al primero

print(otraLista)

otraLista2 =[1,42,33,70,5,6,7,8,229,210]

otraLista2.sort() # Ordenar la lista de menor a mayor

print (otraLista2)

otraLista2.pop(0) # Eliminar el elemento ubicado en el indice 0

print (otraLista2)

otralista3 = [1,2,3,4,5,6,7,8,[11,12,13]]

print(otralista3)

print(otralista3[8][0])

otralista3.extend([[20,21,22]])

print(otralista3)

print(otralista3[9][1])

lista5 = [1, 2, 3, 4, 5, 3, 3]

print(list(set(lista5)))

lista = [1, 2, 3, 4, 5]

sublista = lista[1:4]

sublista.reverse()

lista[1:4] = sublista

print(sublista)

frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]

print("".join(frutas))

print([-num for num in range(1, 11)])

lista1 = [1, 2, 3] 

lista2 = ['a', 'b', 'c']

print(list(zip(lista1, lista2)))

print(list(range(1, 6)))

palabras = ["HoLa", "MUNDO", "pYThon"]

print([palabra.upper() for palabra in palabras])