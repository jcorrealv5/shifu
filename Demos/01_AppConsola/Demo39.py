import json, os
from urllib import request, error

#Demo 38: Cliente HTTP que obtiene el JSON de una Servicio Web Dinamico: Array de Objetos
print("Demo 38: Cliente HTTP que obtiene el JSON de una Servicio Web Dinamico: Array de Objetos")
url = input("Ingresa la Url con el Servicio que devuelve un JSON: ")
try:
    rptaHttp = request.urlopen(url)
    if(rptaHttp is not None and rptaHttp.status==200):
        rptaBytes = rptaHttp.read()
        objJson = json.loads(rptaBytes)
        nLista = len(objJson)
        campos = [key for key in objJson[0]]
        nCampos = len(campos)
        rpta = []
        rpta.append(";".join(campos))
        errores = []
        for i in range(nLista):
            try:
                objFila = objJson[i]
                fila = []
                for j in range(nCampos):
                    if(campos[j] in objFila):
                        fila.append(str(objFila[campos[j]]).replace("\n"," "))
                    else:
                        fila.append("")
                rpta.append(";".join(fila))
            except Exception as errorFila:
                errores.append(i)
                print("Error Fila: ", errorFila)
        print(rpta)
        print(errores)
        archivo = os.path.basename(url) + ".csv"
        with open(archivo, "w") as file:
            file.write("\n".join(rpta))
        print("Se creo el archivo: ", archivo)
    else:
        print("No existe conexion al sitio")
except error.HTTPError as errorHttp:
    print("Error HTTP: ", errorHttp)
except ValueError as errorValor:
    print("Error Valor: ", errorValor)
except Exception as errorGeneral:
    print("Error Generico: ", errorGeneral)