from services import service08MySqlplantilla as service
from models.plantilla import Plantilla


print("------TRABAJAR CON PLANTILLA------")
servicio = service.ServiceMySqlPlantilla()
plantilla = servicio.getPlantilla()


print("Escoja una opción:")
print("1 - Mostrar los datos de la plantilla")
print("2 - Modificar salario de la plantilla")
opcion = int(input())
if ( opcion == 1):
    for emp in plantilla:
        print(f"{emp.apellido}, {emp.funcion}, {emp.salario}")
elif ( opcion == 2):
    print("Introduzca CÓDIGO DE HOSPITAL")
    hosp_cod = int(input())
    print("Introduzca INCREMENTO")
    incremento = int(input())
    registro = servicio.UpdateSalario(incremento, hosp_cod)
    print(f"Plantilla modificada: {registro}")

print ("Fin de PROGRAMA")

