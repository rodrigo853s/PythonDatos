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
print ("2 - Borrar Doctor")
print ("3 - Modificar Doctor")
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
    reg = servicio.insertarDoctor(iddoctor, ape, espe, hosp, sala)
    print(f"Doctores insertados; {reg}")
elif (opcion == 2):
    print("Introduzca ID a eliminar")
    iddoctor = int(input())
    registros = servicio.eliminarDoctor(iddoctor)
    print(f"Doctores eliminados: {registros}")
elif (opcion == 3):
    print("Introduzca ID a modificar")
    iddoctor = int(input())
    print("Nuevo Apellido?")
    ape = input()
    print("Nueva Especialidad?")
    espe = input()
    print("Nuevo Salario?")
    sala = int(input())
    print("Hospital?")
    hosp = int(input())
    registros = servicio.modificarDoctor(iddoctor, ape, espe, sala, hosp)
    print(f"Doctores modificados: {registros}")
print("Fin de programa")