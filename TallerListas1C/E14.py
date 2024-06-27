palabras = ["Python", "es", "un", "lenguaje", "de", "programación"]

resultado = []

for i, palabra in enumerate(palabras):

    if i % 2 == 0:

        resultado.append(palabra.upper())

    else:

        resultado.append(palabra.lower())

print(resultado)
