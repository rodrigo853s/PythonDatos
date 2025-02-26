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
    