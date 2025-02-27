import oracledb
from models import hospital as model

class ServiceOracleHospital:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
    
    def getAllHospital(self):
        sql = "select * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        list = []
        for row in cursor:
            hosp = model.Hospital()
            hosp.codigo = row[0]
            hosp.nombre = row[1]
            hosp.direccion = row[2]
            hosp.telefono = row[3]
            hospcamas = row[4]
            list.append(hosp)
        cursor.close
        return list






