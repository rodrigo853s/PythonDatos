# Sobre models creamos una nueva clase llamada doctor y un servicio en services
# una vez creados, venimos al main

from services import service05oracledoctores as service
from models import doctor as model

print("Esto es un CRUD de DOCTORES")
servicio = service.ServiceOracleDoctores()
doctores = servicio.getAllDoctores()
for doc in doctores:
    print(f"{doc.apellido}, {doc.especialidad}")
print("Fin de programa")

# Ahora creamos un nuevo servicio para insertar doctores en service05doctores.py y volvemos
print ("1 - Insertar Doctor")
print("Seleccione opcion")
opcion = int(input())
if (opcion == 1):
    print("Id Doctor")
    iddoctor = int(input())
    print("Apellido?")
    ape = input()
    print("Especialidad?")
    espe = input()
    print("Salario?")
    sala = int(input())
    print("Hospital?")
    hosp = int(input())
    reg = servicio.insertarDoctor(iddoctor, ape, espe, sala, hosp)
    print(f"Doctores insertados; {reg}")
print("Fin de programa")