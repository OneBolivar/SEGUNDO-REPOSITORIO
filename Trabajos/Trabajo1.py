NumeroPersonas = int(input("¿Cuántas personas desea registrar?: "))
ConocimientosBasicos = False
for i in range (NumeroPersonas):
    Nombre = input("Ingrese su nombre: ")
    Edad = int(input("Ingrese su edad: "))
    while Edad <= 0:
        print("Por favor ingrese una edad valida")
        Edad = int(input("Ingrese su edad: "))
    validador = input("¿Tiene conocimientos básicos de computación?: ")
    if validador == "si":
        ConocimientosBasicos = True
    if (Edad >= 15) and (ConocimientosBasicos == True):
        print("Puede participar en el taller ")
    else:
        print("No cumple los requisitos ")
print("Proceso finalizado")





