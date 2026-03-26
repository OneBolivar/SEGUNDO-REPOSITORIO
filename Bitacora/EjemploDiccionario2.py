Running = True
Estudiantes = {}
id = 0
calif = 0
while Running:
    nombre = input("Ingrese su nombre: ")
    calificacion = float(input("Ingrese la calificacion: "))

    Estudiantes[id] = {
        "nombre" : nombre,
        "calificacion" : calificacion
    }
    id += 1
    calif += calificacion
    
    salir = input("Desea añadir a otro estudiante (yes/no): ").lower
    if salir == "No":
        print("Programa finalizado")
        Running = False
    
    print(calif/id)  
    Result = 0  
    for Estudiante, into in Estudiantes.items():
        Result += into["calificacion"]
        
    operacion = Result/id  
    print(f"El promedio de calificaciones es: {operacion}")