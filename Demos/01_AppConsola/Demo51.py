import sys
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

print("Demo 51: Consulta de una tabla usando Select en la Aplicacion")

archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogDemo51.txt"

con = clienteSQL(archivoConfig, archivoLog)
listaCursos = con.EjecutarComandoCadena("Select * From Curso")
if(listaCursos is not None):
    print(listaCursos)
else:
    print("Ocurrio un Error al ejecutar el comando. Ver Log")