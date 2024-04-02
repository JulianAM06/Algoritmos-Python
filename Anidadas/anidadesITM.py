carrera = int(input("Ingresa\n1--Civil\n2--Mecanica\n3--Odontologia\n4--Administracion\n5--Derecho\n6--Sistema\n7--Medicina\nPara saber la carrera: "))
valorMatricula = int(input("Ingresa valor de Matricula: "))
valorBachillerato = int(input("Ingresa valor de Bachillerato: "))
estrato = int(input("Ingresa Estrato: "))



if carrera == 1:

    if estrato >= 4:

        print(valorMatricula)

    else:

        valorTotal = valorMatricula - (valorMatricula * 0.15)

        print(valorTotal)
        

elif carrera == 2:

    if estrato >= 1 or estrato <=4:

         valorTotal = valorMatricula - (valorMatricula * 0.20)

    else:

        valorTotal = valorMatricula

    print(valorTotal)


elif carrera == 3:

    valorTotal = valorMatricula + (valorMatricula * 0.40)

    print(valorTotal)


elif carrera == 4:

    valorTotal = valorMatricula + (valorBachillerato * 0.20)

    print(valorTotal)


else:

    print(valorMatricula)







