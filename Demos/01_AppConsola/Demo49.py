import pyodbc as db

print("Demo 49: Conectar a BD_DACP_2025 y traer una lista de Alumnos")
driver="ODBC Driver 17 for SQL Server"
servidor="LAPTOP-QSG034LN\SQLSERVER"
usuario="Usuario_BD_DACP_2025"
clave="123456"
basedatos="BD_DACP_2025"
cadenaConexion = f"driver={driver};server={servidor};uid={usuario};pwd={clave};database={basedatos}"
con = db.connect(cadenaConexion)
print(con)
cmd = con.cursor()
print(cmd)
cursor = cmd.execute("Select * From Alumno")

#Crear una lista para grabar en un archivo de texto
listaCsv = []

#Obtener las Cabeceras o Nombres de Campos de la Consulta
cabeceras = cursor.description
nCabeceras = len(cabeceras)
campos = []
for j in range(nCabeceras):
    campos.append(cabeceras[j][0])
print(campos)
listaCsv.append(",".join(campos))

#Obtener las Registros de la Consulta
lista = cursor.fetchall()

#Recorrer todos los registros y presentar sus campos con valores
nRegistros = len(lista)
for i in range(nRegistros):
    tupla = lista[i]
    nCampos = len(tupla)
    fila = []
    for j in range(nCampos):
        print(campos[j] + " = " + str(tupla[j]))
        fila.append(str(tupla[j]))    
    print("_" * 50)
    listaCsv.append(",".join(fila))

#Grabar el Archivo de Texto con la data de los alumnos
with open("Alumnos.txt", "w") as file:
    file.write("\n".join(listaCsv))
print("Se creo el archivo Alumnos.txt")
