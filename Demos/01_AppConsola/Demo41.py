import os, smtplib
from email.mime.text import MIMEText

#Demo 41: Envio de Correos con Simple Mensaje usando smtplib y MIMEText
print("Demo 41: Envio de Correos con Simple Mensaje usando smtplib y MIMEText")
ruta = "C:/Data/Python/2025_01_PythonMJ/Clases/"
archivoUserPass = os.path.join(ruta, "UserPass.txt")
with open(archivoUserPass,"r") as fileUserPass:
    lineas = fileUserPass.read().split("\n")
    usuario = lineas[0]
    password = lineas[1]
archivoCorreos = os.path.join(ruta, "Correos.txt")
with open(archivoCorreos,"r") as fileCorreos:
    correos = fileCorreos.read().split("\n")
mensaje = MIMEText("Prueba de Correo desde Python. No responder")
mensaje["Subject"] = "DACP 2025"
mensaje["From"] = "Luis.duenash@gmail.com"
mensaje["To"] = ",".join(correos)
print("Enviando Correos a: ", correos)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as clienteCorreo:
        clienteCorreo.login(usuario, password)
        clienteCorreo.sendmail(usuario, correos, mensaje.as_string())
    print("Se envio el correo a los alumnos")
except Exception as errorCorreo:
    print("Error Correo: ", errorCorreo)