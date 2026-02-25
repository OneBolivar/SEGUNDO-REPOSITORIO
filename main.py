Hacer = int(input("¿Que desea hacer? 1. Registro de personas o 2. Compra de productos: "))
VAL = True
while Hacer == (1 or 2):
        if Hacer == 1:
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
        elif Hacer == 2:
                        NombreUsuario = input("Ingrese su nombre: ")
                        PrecioProducto = float(input("Ingrese el precio del producto: "))
                        CantidadProducto = float(input("Ingrese la cantidad de productos que desea comprar: "))
                        VIP = bool(input("¿Es usted cliente VIP? (si es cliente VIP escriba: True, sino, pulse la tecla intro ): "))
                        Subtotal = PrecioProducto * CantidadProducto
                        print("Resumen de la compra:")
                        print("Cliente: ", NombreUsuario)
                        print("Subtotal: ", Subtotal)
                        if (VIP):
                            print("Descuento aplicado: 10%")
                            print("El total a pagar es: ", Subtotal-(Subtotal*0.10))
                        else:
                            print("Descuento aplicado: 0%")
                            print("El total a pagar es: ", Subtotal)  
else:
      print("Ingrese solo el numero de las opciones correspondientes: ")


print("TIENE UN ERROR; ARREGLAR ")










           