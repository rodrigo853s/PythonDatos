# Queremos INSERTAR, por lo que necesitamos Número, nombre y localidad
# El servicio es el que INSERTA. No pintamos nada, por lo que no hemos creado un 
# objeto con los datos necesarios
from services import service04oracledepartamentos as service
print("-----------SERVICE ORACLE DEPARTAMENTOS-------------")
servicio = service.ServiceOracleDepartamentos()

print("Insertar departamento")
print("ID departamento")
numero = int(input())
print("Nombre departamento")
nombre = input()
print("Localidad departamento")
localidad = input()
# Guardamos en una variable
afectados = servicio.insertarDepartamento(numero, nombre, localidad)
print(f"Departamentos insertados: {afectados}")
print("Fin de programa")




