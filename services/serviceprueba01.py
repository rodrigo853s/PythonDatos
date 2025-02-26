from models import mascota
# Este servicio será el que tendrá métodos para ser utilizados 
# el en MAIN

def getSaludo():
    return "Welcome to the jungle!"

def getMascota():
    dato = mascota.Mascota()
    dato.nombre = "Toby"
    dato.raza = "dobermann"
    dato.edad = 3
    return dato

def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Felisa"
    dato.raza = "caniche"
    dato.edad = 4
    return dato
