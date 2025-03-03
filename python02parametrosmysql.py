import pymysql
connection = pymysql.connect(host='localhost', port=3306, user='getafe', 
password='mysql', database='HOSPITAL')


cursor = connection.cursor()
sql = "select * from EMP where salario >= %s"
print("Salario?")
salario = int(input())
cursor.execute(sql, (salario, ))

for row in cursor:
    print(f"Apellido: {row[1]}, Oficio: {row[2]}, Salario: {row [5]}")
cursor.close()
connection.close()
print("Fin de Programa")