import json
from urllib import request, error

#Demo 37: Cliente HTTP que obtiene el JSON de una Servicio Web Fijo
print("Demo 37: Cliente HTTP que obtiene el JSON de una Servicio Web Fijo")
url = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01288PM/json"
try:
    rptaHttp = request.urlopen(url)
    if(rptaHttp is not None and rptaHttp.status==200):
        rptaBytes = rptaHttp.read()
        objJson = json.loads(rptaBytes)
        lista = objJson["periods"]
        nLista = len(lista)
        print(objJson["config"]["title"])
        for i in range(nLista):
            objFila = lista[i]
            print(f"{objFila['name']} = {objFila['values'][0]}")
    else:
        print("No existe conexion al sitio")
except error.HTTPError as errorHttp:
    print("Error HTTP: ", errorHttp)
except ValueError as errorValor:
    print("Error Valor: ", errorValor)
except Exception as errorGeneral:
    print("Error Generico: ", errorGeneral)