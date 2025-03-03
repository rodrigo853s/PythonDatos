import pyodbc
#connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + localhost + ';DATABASE=' +
                            #HOSPITAL + ';UID=' + SA + ';PWD=' + 'Getafe12345@@')
connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
                     
print("Funciona SQL server???")

cursor = connection.cursor()
sql = "select * from EMP"
cursor.execute(sql)
for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}")
cursor.close()
connection.close()
print("Fin de Programa")