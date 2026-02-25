
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
