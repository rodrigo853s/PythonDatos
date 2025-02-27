# Queremos INSERTAR, por lo que necesitamos Número, nombre y localidad
# El servicio es el que INSERTA. No pintamos nada, por lo que no hemos creado un 
# objeto con los datos necesarios
from services import service04oracledepartamentos as service
from models import departamento


print("-----------SERVICE ORACLE DEPARTAMENTOS-------------")
servicio = service.ServiceOracleDepartamentos()
print("1 - Insertar departamento")
print("2 - Buscar departamento")
print("3 - Borrar departamento")
print("4 - Modificar departamento")
print("Selecione una opción")
opcion = int(input())
if (opcion == 1 ):

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
elif(opcion == 2):
    print("Buscador de deptos por ID")
    print("Introduzca ID")
    iddept = int(input())
    #declaramos una variable para guardar el departamento
    dept = servicio.buscarDepartamentoId(iddept)
    print(f"{dept.numero}, {dept.nombre}, {dept.localidad}")
elif(opcion == 3 ):
    print("Eliminador de deptos por ID")
    print("Introduzca ID")
    iddept = int(input())
    #declaramos una variable para guardar el departamento
    afectados = servicio.borrarDepartamento(iddept)
    print(f"Departamentos borrados: {afectados}")
elif(opcion ==4 ):
    print("Modificador de deptos por ID")
    print("Introduzca ID")
    iddept = int(input())
    print("Nuevo Nombre")
    nombre = input()
    print("Localidad")
    localidad = input()

    modificados = servicio.modificarDepartamento(iddept, nombre, localidad)
    print(f"Departamentos modificados:  {modificados}")

print("Fin de programa")




