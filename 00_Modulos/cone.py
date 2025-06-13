import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-F4UDH2D;"  # Cambia por tu servidor
    "DATABASE=BD_DACP_2025;"
    "Trusted_Connection=yes;"
)
print(conn)
cursor = conn.cursor()
cursor.execute("SELECT GETDATE()")
print(cursor.fetchone())

conn.close()


print(pyodbc.drivers())
