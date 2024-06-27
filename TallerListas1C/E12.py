palabras = ["hola", "mundo", "holanda", "python", "holístico"]

subcadena = "hol"

for i in palabras:

    if not subcadena in i:

        palabras.remove(i)

print(palabras)