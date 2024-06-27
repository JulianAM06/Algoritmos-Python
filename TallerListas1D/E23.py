listaMixta = [3, "banana", 1, "manzana", 4, "cereza", 2]

listaNumerica = []

listaString = []

for i in listaMixta:

    if isinstance (i, int):

        listaNumerica.append(i)

    else:

        listaString.append(i)

listaNumerica.sort()

listaString.sort()

a = listaNumerica + listaString

print(a)

listaNumerica.sort(reverse=True)

listaString.sort(reverse=True)

b = listaNumerica + listaString

print(b)



