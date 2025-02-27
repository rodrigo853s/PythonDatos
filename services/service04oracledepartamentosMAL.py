# Va a ser una clase este servicio

import oracledb
from models import departamento

class ServiceOracleDepartamentos:
    # Sólo va a tener u método: conexión
    def __init__(self):
        # Creamos un objeto connection
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def insertarDepartamento(self, numero, nombre, localidad):
        sql = "insert into DEPT values (:id, :nombre, :localidad)"
        # Ahora creo un cursos, que se recupera a partir de self.connection
        cursor = self.connection.cursor()
        # Ejecutamos la consulta
        cursor.execute(sql, (numero, nombre, localidad))
        # Guardamos los registros afectados en una variable (opcional)
        registros = cursor.rowcount
        # Si queremos que sea permanente:
        self.connection.commit()
        # cerramos el cursor y devolvemos los registros
        cursor.close()
        return registros
    # No es necesario cerrar la conexión; se hace automáticamente


# Necesito un método nuevo en el servicio que nos devuelva el número, el nombre y la localidad
# del departamento encontrado. No podemos devolver los tres datos a la vez.
# Necesito un modelo con esos datos.
# creamos la clase departamento.py (lo importo en la línea 4)

    def buscarDepartamentoId(self, numero):
        sql = "select * from DEPT where DEPT_NO = :p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        row = cursor.fetchone()
        # Creamos nuestro Departamento MODELO
        modelo = departamento.Departamento()
        # Asignamos los datos del row al modelo
        modelo.numero = row[0]
        modelo.nombre = row[1]
        modelo.localidad = row[2]
        cursor.close
        return modelo
    # Probamos la funcionalidad en el main04


# Ahora un DELETE
    def borrarDepartamento(self, numero):  # self indica que utilizaremos la conexión
        sql = "delete from DEPT where DEPT_NO = :p1"
        cursor = self.connection.cursor()
        # Ejecutamos la consulta
        cursor.execute(sql, (numero,))
        registros = cursor.rowcount
        self.connection.commit()
        # cerramos el cursor y devolvemos los registros
        cursor.close()
        return registros

# Ahora modificaremos un departamento por su ID

    def modificarDepartamento(self, numero, nombre, localidad):
        sql = "update DEPT set DNOMBRE= :p1, LOC= :p2 where DEPT_NO= :p3"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, numero))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
# Mostrar todos los departamentos
    def getAllDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        # Creamos una lista para almacenar cada depto
        datos = []
        # Recorremos el cursor de datos
        for row in cursor:
            # Por cada vuelta de bucle debemos crear un nuevo objeto departamento,
            # no que reutilice el mismo
            dept = departamento.Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            # Esas filas se pierden en el tiempo, asi que las voy almacenando
            datos.append(dept)
        cursor.close()
        return datos
