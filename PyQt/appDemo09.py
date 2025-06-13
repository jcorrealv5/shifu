import os
import pyodbc as db

driver="ODBC Driver 17 for SQL Server"
servidor="DESKTOP-F4UDH2D"
usuario="sa"
clave="123456"
basedatos="BD_DACP_2025"
cadenaConexion = f"driver={driver};server={servidor};uid={usuario};pwd={clave};database={basedatos}"
con = db.connect(cadenaConexion)
cmd = con.cursor()

print("Demo 09: Insertar Fotos desde el File System a la Base de Datos")
rutaFotos = "C:/Users/jhonf/Documents/Shifu/Alumnos"
archivos = os.listdir(rutaFotos)
for archivo in archivos:
    print(archivo)
    id = archivo.split(".")[0]
    nombreCompleto = os.path.join(rutaFotos, archivo)
    with open(nombreCompleto,"rb") as file:
        buffer = file.read()
    sql = "exec uspAlumnoActualizarFoto @IdAlumno=?,@Foto=?"
    params = (id, db.Binary(buffer))
    cursor = con.execute(sql, (params))
    con.commit()  
print("Se migro todos los archivos")