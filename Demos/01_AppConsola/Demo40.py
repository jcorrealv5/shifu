from urllib import request
import json

def post_data(url, data, headers={'Content-Type':'application/json'}):
    bindata = data if type(data) == bytes else data.encode('utf-8')
    req = request.Request(url, bindata, headers, method="POST")
    resp = request.urlopen(req)
    return resp.read(), resp.getheaders()

#Demo 40: Cliente HTTP que ejecuta un POST para enviar correo
print("Demo 40: Cliente HTTP que ejecuta un POST para enviar correo")
url = "https://funciones.grupomok.com/api/Correo/EnvioCorreo"
try:
    data = json.dumps({"idUser": "luis.duenas","codFrom": 1, "to": "luis.duenash@gmail.com", "subject": "POST","body": "Esto es una Prueba de POST"})
    rptaData, rptaCabecera = post_data(url, data, headers={'Content-Type':'application/json'})
    print(rptaData)
except Exception as errorGeneral:
    print("Error General: ", errorGeneral)