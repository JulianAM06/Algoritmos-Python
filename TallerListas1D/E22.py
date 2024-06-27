import datetime

proyectos = [["Proyecto1", datetime.date(2023, 6, 10)], 
             ["Proyecto2", datetime.date(2023, 7, 15)], 
             ["Proyecto3", datetime.date(2023, 6, 25)]]

mes_actual = datetime.date.today().month # Obtener el mes actual

#dia_actual = datetime.date.today().day # Obtener el día actual
#anio_actual = datetime.date.today().year # Obtener el año actual

print(mes_actual)

proyectos_mes_actual = [proyecto[0] for proyecto in proyectos if proyecto[1].month == mes_actual]

print("Proyectos con fecha de entrega en el mes actual:", proyectos_mes_actual)
