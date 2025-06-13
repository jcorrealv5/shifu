#Demo17: Crear un Archivo de Texto Nuevo
titulo = "Demo17: Crear un Archivo de Texto Nuevo"
print(titulo)
print("_" * len(titulo))
archivo = input("Archivo a grabar el texto: ")
texto = input("Texto a escribir en el archivo: ")
with open(archivo, "w") as file:
    file.write(texto)
print("Se creo el archivo de texto")