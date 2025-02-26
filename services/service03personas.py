# El servicio sólo contendrá métodos
from models import persona
def getPersona():
    #Creamos una nueva persona
    info = persona.Persona()
    info.nombre = "Pepe"
    info.edad = 34
    info.email = "pepe@gmail.com"
    return info
        