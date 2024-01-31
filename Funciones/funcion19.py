def multiplicar_lista(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

mi_lista = [5, 2, 3, 4, 1]
resultado = multiplicar_lista(mi_lista)
print(resultado) 