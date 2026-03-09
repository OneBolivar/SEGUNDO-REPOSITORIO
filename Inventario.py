VALIDADOR = True
#Declaramos una Variable llamada VALIDADOR como Verdadera
NombreProducto = input("Ingrese el nombre del producto: ")   
#Pedimos el nombre de el producto con el input
while VALIDADOR:
#Creamos un bucle While con VALIDADOR para que se repita el proceso que queremos 
    try:
#Iniciamos un try para solucionar un error que se explicara mas adelante  
        PrecioProducto = float(input("Ingrese el precio del producto: "))
#Creamos el paramatro "PrecioProducto"para pedir el precio del producto
        CantidadProducto = int(input("¿Cuantos productos desea comprar?: "))
#Creamos el paramatro "CantidadProducto"para pedir la cantidad del producto
        Total = PrecioProducto*CantidadProducto
#Creamos el parametro Total para hacer el proceso de Precio * Cantidad (producto)
        print("Producto:",NombreProducto,"|Precio Unitario:",PrecioProducto,"|Cantidad:",CantidadProducto,"|Total a pagar:",Total )
#Imprimimos en pantalla el nombre del producto, precio unitario, la cantidad a comprar y el total a pagar
        VALIDADOR = False
        
    except ValueError:
        
        print("¡ERROR! Debe ingresar un número")


   