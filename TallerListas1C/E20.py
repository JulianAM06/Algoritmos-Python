palabras = ["python", "es", "genial", "muy", "bueno"]

for i in palabras:

    if len(i) < 4:

        palabras.remove(i)

print(palabras)