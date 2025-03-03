# Crear un nuevo servicio llamado ServicePlantilla en un servicio service08oraacleplantilla.py
# Crear un modelo para la plantilla, con los siguientes datos:
# PLANTILLAS
#   idPlantilla
#    apellido
#    funcion
#    salario
#    hospital
# El servicio consumirá ORACLE , con dos métodfos
# getPlantilla: Mostrará los datos (listado) de la plantilla
# UpdateSalario: Modificará el salraio de una plantilla con un incremento que le daremos y un número de hospital
# probamos los métodos en un main08plantilla.py.
# Después probamos con MySql y SQL server

import pymysql
from models.plantilla import Plantilla

class ServiceMySqlPlantilla:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', port=3306, user='getafe', password='mysql', database='HOSPITAL')

    def getPlantilla(self):
        sql = "select * from PLANTILLA"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        # DEBEMOS INDICAR EL TIPO DE LISTA QUE ESTAMOS DEVOLVIENDO
        # variable:list[TIPO DE CLASE] = []
        data:list[Plantilla] = []
        for row in cursor:
            emp = Plantilla()
            emp.idPlantilla = row[2]
            emp.apellido = row[3]
            emp.funcion = row[4]
            emp.salario = row[6]
            emp.hospital = row[0]
            data.append(emp)
        cursor.close
        return data

    def UpdateSalario(self, salario, hospital_cod):
        sql = "update PLANTILLA set SALARIO = SALARIO + %s where HOSPITAL_COD = %s"
        cursor = self.connection.cursor()
        cursor.execute(sql, (salario, hospital_cod))
        incrementados = cursor.rowcount
        self.connection.commit()
        cursor.close
        return incrementados
        