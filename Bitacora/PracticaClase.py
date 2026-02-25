Edad = input("Ingrese su edad: ")
Puede_conducir = None
try:
    Edad = int(Edad)

    if (Edad >= 26):
        print("Puedes conducir")
        Puede_conducir = True

    else:
        print("No puedes conducir")
        

    if(Puede_conducir):
        print("Se confirma que usted SI esta habilitado para conducir")
    else:
        print("Se confirma que usted NO esta habilitado para conducir")


except:
    print("El dato ingresado NO es un numero")

