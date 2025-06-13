import sys
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

print("Demo 52: Consulta de una tabla usando Procedimiento Almacenado en SQL")

print("Lista de Cursos")
archivoConfig = r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
archivoLog = r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogDemo51.txt"

con = clienteSQL(archivoConfig, archivoLog)
listaCursos = con.EjecutarComandoCadena("dbo.uspAlumnoListar")
if(listaCursos is not None):
    print(listaCursos)
else:
    print("Ocurrio un error al traer los datos. Ver Log")