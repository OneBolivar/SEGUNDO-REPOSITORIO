Productos = {
    'cono' : 3000,
    'vaso' : 4000,
    'banana split' : 9000   
}
print()
print("Bienvenido a la heladeria Krasel Supra")
print()
print("Estos son nuestros productos: ")
print()
for i, Producto in enumerate(Productos):
    print(f"{i+1} : {Producto}")
Validador = True
while Validador:
    print()
    PedirProducto = int(input("Ingrese su pedido: "))
    PedirCantidad = int(input("¿Cuantos comprara?: "))
    TotalPagar = PedirProducto * PedirCantidad  
    Seguir = input("¿Desea pedir otra cosa?: ").lower() .strip() 
    if Seguir == "no":
        Validador = False
    