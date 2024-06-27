fibonacci = [0, 1]

for i in range(2, 10):

    siguiente = fibonacci[-1] + fibonacci[-2]

    fibonacci.append(siguiente)

print("Lista de los primeros 10 números de Fibonacci:", fibonacci)