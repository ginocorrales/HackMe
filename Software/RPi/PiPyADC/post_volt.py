import pyodbc

dsn = 'src' 
user = 'hacker@hackillinois2019'
password = 'gOOns412' 
database = 'HackIllinoisTest' 

connString = 'DSN={0};UID={1};PWD={2};DATABASE={3};'.format(dsn,user,password,database)

conn = pyodbc.connect(connString)

cursor = conn.cursor()

sql = "INSERT INTO dbo.voltages (CustomerID, Voltage) VALUES (?, ?)" 
val = (1, 5.0823864) 
cursor.execute(sql, val) 

conn.commit()
