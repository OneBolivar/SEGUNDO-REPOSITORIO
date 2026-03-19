Productos = {
    'cono' : 3000,
    'vaso' : 4000,
    'banana split' : 9000   
}
Historial = {
    "cono" : 0,
    "vaso" : 0,
    "banana_split" : 0, 
}
Historial_clientes = {
    "clientes" : 0,
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
       Historial_clientes["total_pagar"] += TotalPagar
       Historial_clientes["clientes"] += 1 
    elif PedirProducto == 2 :
       Historial["vaso"] += PedirCantidad 
       TotalPagar = PedirCantidad * 4000
       Historial_clientes["total_pagar"] += TotalPagar
       Historial_clientes["clientes"] += 1 
    elif PedirProducto == 3 :
       Historial["banana_split"] += PedirCantidad 
       TotalPagar = PedirCantidad * 9000    
       Historial_clientes["total_pagar"] += TotalPagar
       Historial_clientes["clientes"] += 1 
    Seguir = input("¿Desea pedir otra cosa?: ").lower() .strip() 
    Max_pedido = max(Historial , key= Historial.get)
    if Seguir == "no":
        print("El total a pagar es de: ", Historial_clientes['total_pagar'])
        print("El total de clientes atendidos es de: ", Historial_clientes['clientes'])
        print("El producto que se vendio mas veces fue:",Max_pedido)
        Validador = False
