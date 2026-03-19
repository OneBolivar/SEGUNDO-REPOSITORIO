Productos = {
    'cono' : 3000,
    'vaso' : 4000,
    'banana split' : 9000   
}

Historial = {
    "cono" : 0,
    "vaso" : 0,
    "banana_split" : 0,
    "total_pagar" : 0
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
    if PedirProducto == 1 :
       Historial["cono"] += PedirCantidad 
       TotalPagar = PedirCantidad * 3000
       Historial["total_pagar"] += TotalPagar
    if PedirProducto == 2 :
       Historial["vaso"] += PedirCantidad 
       TotalPagar = PedirCantidad * 4000
       Historial["total_pagar"] += TotalPagar
    if PedirProducto == 3 :
       Historial["banana_split"] += PedirCantidad 
       TotalPagar = PedirCantidad * 9000    
       Historial["total_pagar"] += TotalPagar
        
        
    Seguir = input("¿Desea pedir otra cosa?: ").lower() .strip() 
    if Seguir == "no":
        print(Historial)
        Validador = False
