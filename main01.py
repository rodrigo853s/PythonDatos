from services import serviceprueba02 as serv
from models import mascota
saludo = serv.getSaludo()
print("Todo OK, " + saludo)

perro = serv.getMascota()
perra = serv.getMascota2()
print(perro.nombre, perro.raza, perro.edad)
print(perra.nombre, perra.raza, perra.edad)

