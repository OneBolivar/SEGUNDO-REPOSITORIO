Asistencia_semanal_baja = []
Asistencia_semanal_media = []
Asistencia_semanal_alta = []
for i in range(5):

    Persona = input("Ingrese su nombre: ")
    Asistencia = int(input("¿Cuantos dias asistio esta semana?: "))
    Tiempo = float(input("¿Cuantos minutos (en promedio) duro entrenando?: "))
    if Asistencia < 3:
        Asistencia_semanal_baja.append(Persona)
    if Asistencia >= 3 and Asistencia < 5 :
        print()
        Asistencia_semanal_media.append(Persona)        
    if Asistencia >= 5:
        Asistencia_semanal_alta.append(Persona)
print("Las personas que tienen compromiso bajo son: ", Asistencia_semanal_baja)
print("Las personas que tienen compromiso bajo son: ", Asistencia_semanal_media)
print("Las personas que tienen compromiso bajo son: ", Asistencia_semanal_alta)