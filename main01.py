from services import serviceprueba02 as serv
from models import mascota
saludo = serv.getSaludo()
print("Todo OK, " + saludo)

perro = serv.getMascota()
perra = serv.getMascota2()
print(perro.nombre, perro.raza, perro.edad)
print(perra.nombre, perra.raza, perra.edad)

# Necesitamos mostrar en el MAIN los datos de una PERSONA
# Una persona tienen como propiedades: nombre, edad, email

# Necesito un servicio service03personas.py que nos devolverá una 
# persona con un método llamado getPersona()

# Creamos un MAIN main03personas.py y pdeimos los datos de la persona al
# servicio y los dibujamos