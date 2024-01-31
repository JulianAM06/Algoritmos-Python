lista = [1,2,4,5.98,7,9,50,7,6,23,7]

print(type(lista))
print(lista)

listados = [4,5,8,7,84]

print(type(listados))
print(listados)


print(lista[4]) # Se usa para conocer el valor de la posicion en la lista

print(listados[3]) # Se usa para conocer el valor de la posicion en la lista

lista [3] = "matias" # Se usa para modificar el valor en esa posicion
print(lista)


letras = ["a", "e", "i","o","u"]

print("i" in letras) # Se usa para averiguar si esa variable existe en la lista TRUE/FALSE

print(lista[1:4]) # Se usa para imprimir los datos en el rango indicado

letras.append("z") # Se usa para ingresar esa variable a la lista original
letras.append(6)
print(letras)

listaNueva = listados + letras # Se usa para sumar dos listas y crear una nueva
print(listaNueva)

listaNueva.insert(2, "nuevo elemento") # Se usa para ingresar un nuevo elemento indicando la pocision
print(listaNueva)

del(listaNueva[5]) # Se usa para eliminar un elemtento en la posicion indicada
print(listaNueva)

print(len(listaNueva)) # Se usa para saber la cantidad de elementos en la lista

print(len(lista)) # Se usa para saber la cantidad de elementos en la lista
#print(min(lista))
#print(max(lista))
print(lista.count(7)) # Se usa para saber cuantos elementos existen de la variable en la lista
print(lista.index(23)) # Se usa para saber en que posicion de la lista se encuentra la variable


lista = [1,2,4,5.98,7,9,50,7,6,23,7]


print(lista)


lista.sort()

print(lista)

lista.reverse()

print(lista)