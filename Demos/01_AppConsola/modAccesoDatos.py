import os
import pyodbc as db
from modUtilidades import beLog, Log

class clienteSQL():
    def __init__(self, archivoConfig, archivoLog):
        self.CadenaConexion = ""
        self.ArchivoLog = archivoLog
        try:
            if(os.path.isfile(archivoConfig)):
                with open(archivoConfig, "r") as file:
                    lineas = file.read().split("\n")
                diccionario = {}
                for linea in lineas:
                    campos = linea.split("=")
                    diccionario[campos[0]] = campos[1]
                self.CadenaConexion = "driver={0};server={1};uid={2};pwd={3};database={4}".format(diccionario["driver"],diccionario["servidor"],diccionario["usuario"],diccionario["clave"],diccionario["basedatos"])
            else:
                print("No existe el archivo Config")
        except Exception as errorgeneral:
            obeLog=beLog("modAccesoDatos", "clienteSQL")
            obeLog.setLog("__init__", str(errorgeneral))
            Log.saveLog(obeLog, self.ArchivoLog)
    
    def EjecutarComandoCadena(self, sql):
        rpta = None
        try:            
            con = db.connect(self.CadenaConexion)
            cmd = con.cursor()
            cursor = cmd.execute(sql)
            cabeceras = cursor.description
            nCabeceras = len(cabeceras)
            campos = []
            for j in range(nCabeceras):
                campos.append(cabeceras[j][0])
            rpta = []
            rpta.append(",".join(campos))
            
            lista = cursor.fetchall()
            
            nRegistros = len(lista)
            for i in range(nRegistros):
                tupla = lista[i]
                nCampos = len(tupla)
                fila = []
                for j in range(nCampos):
                    fila.append(str(tupla[j]))    
                rpta.append(",".join(fila))
        except Exception as errorgeneral:
            obeLog=beLog("modAccesoDatos", "clienteSQL")
            obeLog.setLog("EjecutarComandoCadena", str(errorgeneral))
            Log.saveLog(obeLog, self.ArchivoLog)
        return rpta