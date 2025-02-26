# Necesitamos mostrar en el MAIN los datos de una PERSONA
# Una persona tienen como propiedades: nombre, edad, email

# Necesito un servicio service03personas.py que nos devolverá una 
# persona con un método llamado getPersona()

# Creamos un MAIN main03personas.py y pdeimos los datos de la persona al
# servicio y los dibujamos
from services import service03personas as serv
from models import persona

person = serv.getPersona()
print(person.nombre, person.edad, person.email)
print(f"{person.nombre}, {person.edad}, {person.email}")


