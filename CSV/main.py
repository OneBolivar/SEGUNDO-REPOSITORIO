import csv

name = input("Ingrese su nombre: ")
clan = input("Ingrese el nombre de su clan: ")

ruta = '/home/Cohorte5/Escritorio/Bolivar/CSV'

#Escritura
with open('ruta', 'w', newline = '', encoding='utf-8') as fileCoders:
    writer = csv.DictWriter(fileCoders, fieldnames=["name", "clan"])
    writer.writeheader()
    writer.writerow({
        "name": name, 
        "clan": clan
        })
    
#Lectura
with open('ruta', 'r', encoding='utf-8') as fileCoders:
    reader = csv.DictReader(fileCoders)
    for row in reader:
        print(row["name"], row["clan"])