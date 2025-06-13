import sys
sys.path.append("../00_Modulos")
from modUtilidades import beLog, Log
import json
from urllib import request

url = input("Ingresa la URL con el JSON: ")
try:
    rptaHttp = request.urlopen(url)
    if(rptaHttp is not None and rptaHttp.status==200):
        rptaBytes = rptaHttp.read()
        objJson = json.loads(rptaBytes)
        print(objJson)
except Exception as errorGeneral:
    print("Error: ", errorGeneral)
    obeLog = beLog("Demo45", "Demo45")
    obeLog.setLog("Load", str(errorGeneral))
    Log.saveLog(obeLog, "Log_Demo45.txt")