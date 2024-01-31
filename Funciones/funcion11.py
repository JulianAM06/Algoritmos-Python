def ValidarContraseña(password):
    
    largo = False
    mayuscula = False
    numerico = False
    
    if len(password) > 8:
        largo = True
        
    for i in range(len(password)):
        
        if password[i].isupper():
            mayuscula = True
            
        if password[i].isnumeric():
            numerico = True
            
    if largo == True and mayuscula ==True and numerico ==True:
         return True
     
    else:
        return False
    
       
comprobar = True

while comprobar == True:   
    
    password = (input("Ingrese contraseña segura: ")) 
    Validar = ValidarContraseña(password)
    
    if Validar == True:
        comprobar = False
        print("La contraseña es segura")
    
    else:
        print("La contraseña no es segura")