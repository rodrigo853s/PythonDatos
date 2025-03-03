from services import service07mysqlempleados as service
from models.empleados import Empleado


print("------Esto es un TEST de EMPLEADOS------")
servicio = service.ServiceMysqlEmpleados()
empleados = servicio.getEmpleados()

for emp in empleados:
    print(f"{emp.apellido}, {emp.oficio}, {emp.salario}")
print("Salario?")
salario = int(input())
empleados = servicio.getEmpleadosSalario(salario)
for emp in empleados:
    print(f"{emp.apellido}, {emp.oficio}, {emp.salario}")


print ("Fin de PROGRAMA")

