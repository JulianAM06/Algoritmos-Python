n1 = int(input("Ingresa primer numero: ")) 
n2 = int(input("Ingresa segundo numero: ")) 
n3 = int(input("Ingresa tercer numero: ")) 

if n2 > n1:

    if n2 < n3:

        s1 = n2 - n1

        s2 = n2 - n3

        if s2 < 0:

            ns2 = s2 * -1

            if ns2 > s1:

                print("Ganador", n2)
                print("Segundo", n1)

            elif ns2 == s1:

                print("Ganador", n2)
                print("Empate")

            else:

                print("Ganador", n2)
                print("Segundo", n3)

if n2 < n1:

    if n2 > n3:

        s1 = n2 - n1

        s2 = n2 - n3

        if s1 < 0:

            ns1 = s1 * -1

            if ns1 > s2:

                print("Ganador", n2)
                print("Segundo", n3)

            elif ns1 == s2:

                print("Ganador", n2)
                print("Empate")

            else:

                print("Ganador", n2)
                print("Segundo", n1)


if n1 > n2:

    if n1 < n3:

        s1 = n1 - n2

        s2 = n1 - n3

        if s2 < 0:

            ns2 = s2 * -1

            if ns2 > s1:

                print("Ganador", n1)
                print("Segundo", n2)

            elif ns2 == s1:

                print("Ganador", n1)
                print("Empate")

            else:

                print("Ganador", n1)
                print("Segundo", n3)

if n1 < n2:

    if n1 > n3:

        s1 = n1 - n2

        s2 = n1 - n3

        if s1 < 0:

            ns1 = s1 * -1

            if ns1 > s2:

                print("Ganador", n1)
                print("Segundo", n3)

            elif ns1 == s2:

                print("Ganador", n1)
                print("Empate")

            else:

                print("Ganador", n1)
                print("Segundo", n2)


if n3 > n1:

    if n3 < n2:

        s1 = n3 - n1

        s2 = n3 - n2

        if s2 < 0:

            ns2 = s2 * -1

            if ns2 > s1:

                print("Ganador", n3)
                print("Segundo", n1)

            elif ns2 == s1:

                print("Ganador", n3)
                print("Empate")

            else:

                print("Ganador", n3)
                print("Segundo", n2)

if n3 < n1:

    if n3 > n2:

        s1 = n3 - n1

        s2 = n3 - n2

        if s1 < 0:

            ns1 = s1 * -1

            if ns1 > s2:

                print("Ganador", n3)
                print("Segundo", n2)

            elif ns1 == s2:

                print("Ganador", n3)
                print("Empate")

            else:

                print("Ganador", n3)
                print("Segundo", n1)