lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista1 = []

lista2 = []

n = len(lista)

if n % 2 == 0:

    medio = n / 2

    x = int(medio)

    for i in range(0, x):

        lista1.append(lista[i])

    for j in range (x, n):

        lista2.append(lista[j])

elif n % 2 != 0:

    medio = (n / 2) + 0.5

    x = int(medio)

    for i in range(0, x):

        lista1.append(lista[i])

    for j in range (x, n):

        lista2.append(lista[j])

print(lista1)
print(lista2)