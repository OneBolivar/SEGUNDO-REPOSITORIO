SaldoInicial = float(1000)
Numero_Operaciones = int(input("¿Cuantas operaciones desea realizar: ?"))
for i in range (Numero_Operaciones):
    Ejecucion = int(input("Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: "))
    if Ejecucion == 1:
        print("Su saldo actual es de: ", SaldoInicial)
    elif Ejecucion == 2:
        Retiro = float(input("Ingrese monto a retirar: "))
        
    
