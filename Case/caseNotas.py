def determinarNivel(calificacion):
    niveles = {
        19: 'Sobresaliente',
        20: 'Sobresaliente',
        16: 'Muy buena',
        17: 'Muy buena',
        18: 'Muy buena',
        14: 'Buena',
        15: 'Buena',
        12: 'Regular',
        13: 'Regular',
        1: 'Insuficiente',
        2: 'Insuficiente',
        3: 'Insuficiente',
        4: 'Insuficiente',
        5: 'Insuficiente',
        6: 'Insuficiente',
        7: 'Insuficiente',
        8: 'Insuficiente',
        9: 'Insuficiente',
        10: 'Insuficiente',
        11: 'Insuficiente',
    }
    nivel = niveles.get(calificacion, 'desconocido')
    return nivel

calificacion = int (input("Ingrese la calificacion del estudiante: \n19 y 20 Sobresaliente\n16,17 y 18 Muy Buena\n14 y 15 Buena\n12 y 13 Regular\n1-11 Insuficiente\npara verificar su nivel: "))

nivel = determinarNivel (calificacion)

print(f"El nivel de notas del estudiante es: {nivel}")