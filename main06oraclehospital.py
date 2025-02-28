from services import service06oraclehospital as service
from models import hospital as model

print("------Esto es un CRUD de HOSPITALES------")
servicio = service.ServiceOracleHospital()
hospital = servicio.getAllHospital()

print("Seleccione opción")
print("1 - Mostrar Hospitales")
print("2 - Insertar nuevo Hospital")
print("3 - Eliminar Hospital")
print("4 - Modificar Hospital")
opcion = int(input())

if ( opcion == 1):
    for h in hospital:
        print(f"{h.nombre}, {h.direccion}")
elif (opcion == 2):
    print("ID del nuevo hospital:")
    hospid = int(input())
    print("Nombre del nuevo hospital:")
    nombre = input()
    print("Dirección del nuevo hospital:")
    direccion = input()
    print("Telefono del nuevo hospital:")
    telefono = input()
    print("Número de camas del nuevo hospital:")
    camas = int(input())
    registro = servicio.insertarHospital(hospid, nombre, direccion, telefono, camas)
    print(f"Hospitales insertados, {registro}")
elif(opcion == 3):
    print("ID del Hospital a eliminar")
    hospid = int(input())
    reg = servicio.eliminarHospital(hospid)
    print(f"Hospitales eliminados, {reg}")
elif(opcion == 4 ):
    print("ID del Hospital a modificar")
    hospid = int(input())
    print("Nombre hospital:")
    nombre = input()
    print("Dirección  hospital:")
    direccion = input()
    print("Telefono:")
    telefono = input()
    print("Número de camas :")
    camas = int(input())
    reg = servicio.modificarHospital(hospid, nombre, direccion, telefono, camas)
    print(f"Hospitales modificados, {reg}")

print ("Fin de PROGRAMA")

