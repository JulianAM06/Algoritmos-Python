horaslaboradas = int(input("Ingresa horas laboradas: "))

valorHoraLaboral = int(input("Ingresa el valor de la hora laboral: "))

if horaslaboradas <= 40:

    salarioTotal = horaslaboradas * valorHoraLaboral

if horaslaboradas > 40 and horaslaboradas <= 48:

    salarioNormal = 40 * valorHoraLaboral

    horasDoble = horaslaboradas - 40

    pagoHoraExtraDoble = (horasDoble * valorHoraLaboral) * 2

    salarioTotal = salarioNormal + pagoHoraExtraDoble

if horaslaboradas > 48:

    salarioNormal = 40 * valorHoraLaboral

    horasTriple = horaslaboradas - 48

    pagoHoraExtraTriple = (horasTriple * valorHoraLaboral) * 3

    pagoHoraExtraDoble = (8 * valorHoraLaboral) * 2

    salarioTotal = salarioNormal + pagoHoraExtraDoble + pagoHoraExtraTriple

print("El Salario del trabajador es: ", salarioTotal)



    

