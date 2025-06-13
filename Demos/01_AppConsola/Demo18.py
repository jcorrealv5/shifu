from datetime import datetime
import os
#Demo18: Crear un Archivo de Texto Agregable
titulo = "Demo18: Crear un Archivo de Texto Agregable"
print(titulo)
fechaHora = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
archivo = input("Ingresa el Archivo de Texto a Agregar: ")
texto = input("Ingresa el texto a agregar: ")
with open(archivo, "a", encoding="utf-8") as file:    
    file.write("Fecha y Hora: " + fechaHora + "\n")
    file.write("Texto:\n")
    file.write(texto + "\n")
    file.write("_" * 60 + "\n")
print("El texto fue agregado al archivo: ", os.path.basename(archivo))