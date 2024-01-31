def Media (f1, f2, f3):
    
    M = (f1 + f2 + f3) / 3
    
    return M



F1 = int (input("Ingrese factura empresa uno: "))
F2 = int (input("Ingrese factura empresa dos: "))
F3 = int (input("Ingrese factura empresa tres: "))


print(Media(F1, F2, F3))