from models import mascota
# Este servicio será el que tendrá métodos para ser utilizados 
# el en MAIN

def getSaludo():
    return "Welcome to the desert!"

def getMascota():
    dato = mascota.Mascota()
    dato.nombre = "Johnny"
    dato.raza = "pitbull"
    dato.edad = 6
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Jenny"
    dato.raza = "collie"
    dato.edad = 2
    return dato
