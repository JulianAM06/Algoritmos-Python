def es_palindroma(palabra):

    palabra = palabra.lower()  # Convertir la palabra a minúsculas

    palabra_reversa = palabra[::-1]  # Obtener la palabra al revés

    if palabra == palabra_reversa:

        return True
    else:
        return False
    
palabra = input("Ingresa palabra: ")

R = es_palindroma(palabra)

print(R)