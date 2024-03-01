def es_palindromo(palabra):

    palabra = palabra.lower().replace(" ", "")# Convertir la palabra a minúsculas y eliminar espacios

    return palabra == palabra[::-1]


palabra = input("Ingresa palabra o frase para saber si es palindroma: ")

if es_palindromo(palabra):

    print(f"{palabra} es un palíndromo")

else:

    print(f"{palabra} no es un palíndromo")