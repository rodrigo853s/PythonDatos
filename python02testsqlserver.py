import pyodbc
#connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + localhost + ';DATABASE=' +
                            #HOSPITAL + ';UID=' + SA + ';PWD=' + 'Getafe12345@@')
connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost,1433;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
                     
print("Funciona ???")