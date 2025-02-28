import oracledb
from models import hospital as model

class ServiceOracleHospital:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
    
    # MOSTRAR TODOS LOS HOSPITALES
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
            hosp.camas = row[4]
            list.append(hosp)
        cursor.close
        return list

    # INSERTAR UN NUEVO HOSPITAL

    def insertarHospital(self, hospid, nombre, direccion, telefono, camas):
        sql = "insert into HOSPITAL values (:hospid, :nombre, :dir, :telf, :camas)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (hospid, nombre, direccion, telefono, camas))
        registros = cursor.rowcount
        self.connection.commit()
        return registros
    
    # ELIMINAR HOSPITAL

    def eliminarHospital(self, hospid):
        sql = "delete from HOSPITAL where HOSPITAL_COD=:hsp"
        cursor = self.connection.cursor()
        cursor.execute(sql, (hospid,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    # MODIFICAR HOSPITAL

    def modificarHospital(self, hospid, nombre, direccion, telefono, camas):
        sql = "update HOSPITAL set NOMBRE=:p1, DIRECCION=:p2, TELEFONO=:p3, NUM_CAMA=:p4 where HOSPITAL_COD=:p5"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, direccion, telefono, camas, hospid))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros







