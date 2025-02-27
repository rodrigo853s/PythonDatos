from services import service06oraclehospital as service
from models import hospital as model

print("------Esto es un CRUD de HOSPITALES------")
servicio = service.ServiceOracleHospital()
hospital = servicio.getAllHospital()

print("Seleccione opción")
print("1 - Mostrar Hospitales")
opcion = int(input())

if ( opcion == 1):
    for h in hospital:
        print(f"{h.nombre}, {h.direccion}")

print ("Fin de PROGRAMA")

