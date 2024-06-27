mixta = [1, 'hola', 2, 'mundo', 3, '']

for i in mixta:

    if isinstance (i, int):

        mixta.remove(i)

print(mixta)