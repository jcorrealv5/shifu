import os, smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#Demo 42: Envio de Correos con Mensaje HTML con Archivo Adjunto usando smtplib y MIMEMultipart
print("Demo 42: Envio de Correos con Mensaje HTML con Archivo Adjunto usando smtplib y MIMEMultipart")
ruta = "C:/Data/Python/2025_01_PythonMJ/Clases/"
archivoUserPass = os.path.join(ruta, "UserPass.txt")
with open(archivoUserPass,"r") as fileUserPass:
    lineas = fileUserPass.read().split("\n")
    usuario = lineas[0]
    password = lineas[1]
archivoCorreos = os.path.join(ruta, "Correos.txt")
with open(archivoCorreos,"r") as fileCorreos:
    correos = fileCorreos.read().split("\n")
html = "<b>Prueba de Correo desde Python. No responder</b>"
html += "<br/><br/>"
html += "Estimados Alumnos del Curso No se olviden que falta una semana para acabar el mes.<br/>"
html += "Los que pueden pagar ya lo pueden hacer<br/><br/>"
html += "Atentamente: <br/>El Profesor<br/>"

archivoPDF = os.path.join(ruta, "IA_Francia.pdf")
with open(archivoPDF, "rb") as filePdf:
    buffer = filePdf.read()
atachado = MIMEBase("application", "application/pdf")
atachado.set_payload(buffer)
encoders.encode_base64(atachado)
atachado.add_header(
    "Content-Disposition",
    "attachment; filename=IA_Francia.pdf",
)

mensaje = MIMEMultipart()
mensaje["Subject"] = "DACP 2025 HTML Atachado Corregido y A Dormir"
mensaje["From"] = "Luis.duenash@gmail.com"
mensaje["To"] = ",".join(correos)
mensaje.attach(MIMEText(html, "html"))
mensaje.attach(atachado)

print("Enviando Correos a: ", correos)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as clienteCorreo:
        clienteCorreo.login(usuario, password)
        clienteCorreo.sendmail("Luis.duenash@gmail.com", correos, mensaje.as_string())
    print("Se envio el correo a los alumnos")
except Exception as errorCorreo:
    print("Error Correo: ", errorCorreo)