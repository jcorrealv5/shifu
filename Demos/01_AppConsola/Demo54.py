import sys
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

print("Demo 54: Consulta de varias tablas usando un Procedimiento Almacenados en SQL")

archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogDemo51.txt"

con = clienteSQL(archivoConfig, archivoLog)
listas = con.EjecutarComandoListas("uspDACPListas")
for lista in listas:
    print(lista)