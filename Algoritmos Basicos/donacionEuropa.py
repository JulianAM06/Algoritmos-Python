Don_Sol = int(input("Ingrese cantidad de dinero en Soles"))
Don_Dol = int (input("Ingrese cantidad de dinero en Dolares"))
Don_Mar = int (input("Ingrese cantidad de dinero en Marcos"))

Sol_Eur = (Don_Sol*3.52)*1.07
Dol_Eur = (Don_Dol*1.07)
Mar_Eur = (Don_Mar*2.08)*1.07

Don_Total = Sol_Eur+Dol_Eur+Mar_Eur
Don_Com_Euro = ((Sol_Eur+Dol_Eur+Mar_Eur)*30)/100
Don_Adm_Euro = ((Sol_Eur+Dol_Eur+Mar_Eur)*20)/100
Don_Sal_Euro = ((Sol_Eur+Dol_Eur+Mar_Eur)*50)/100

print ("La Donacion total es: ",Don_Total)
print ("La Donacion para el Comedor es: ",Don_Com_Euro)
print ("La Donacion para la Administracion es: ",Don_Adm_Euro)
print ("La Donacion para la Salud es: ",Don_Sal_Euro)