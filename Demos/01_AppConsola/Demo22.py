import os, difflib
#Demo22: Comparar 2 Archivos y Ver sus Diferencias
print("Demo22: Comparar 2 Archivos y Ver sus Diferencias")
archivo1 = input("Ingresa el primer archivo a comparar: ")
if(os.path.isfile(archivo1)):
    archivo2 = input("Ingresa el segundo archivo a comparar: ")
    if(os.path.isfile(archivo2)):
        with open(archivo1, "r", encoding="utf-8") as file1:
            lineas1 = file1.read().split("\n")
        with open(archivo2, "r", encoding="utf-8") as file2:
            lineas2 = file2.read().split("\n")
        html = difflib.HtmlDiff().make_file(lineas1, lineas2)
        archivoHtml = "Diferencias.html"
        with open(archivoHtml, "w", encoding="utf-8") as fileHtml:
            fileHtml.write(html)
        print("Se creo el Archivo Diferencias.html")
    else:
        print("Archivo 2 a comparar No existe")
else:
    print("Archivo 1 a comparar No existe")