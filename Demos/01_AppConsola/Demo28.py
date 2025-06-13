import os, zipfile
#Demo 28: Visor de Textos de Diapositivas de Power Point
print("Demo 28: Visor de Textos de Diapositivas de Power Point")
archivoPPT = input("Ingresa el archivo de Power Point (pptx): ")
if(os.path.isfile(archivoPPT)):
    if(archivoPPT[-5:]==".pptx"):
        nombreCarpeta = os.path.basename(archivoPPT).replace(".pptx","")        
        rutaSalida = os.path.join(os.path.dirname(archivoPPT), nombreCarpeta)
        if(not os.path.isdir(rutaSalida)):
            os.mkdir(rutaSalida)
        zip = zipfile.ZipFile(archivoPPT, "r", zipfile.ZIP_DEFLATED)
        zip.extractall(rutaSalida)
        archivos = zip.namelist()
        zip.close()
        '''
        for i,archivo in enumerate(archivos):
            print(i+1, ":", archivo)
            '''
        print("Total de archivos descomprimidos: ", len(archivos))
        rutaSlides = os.path.join(rutaSalida, "ppt\slides")
        archivosSlides = os.listdir(rutaSlides)
        for i,slide in enumerate(archivosSlides):
            if(slide[:5]=="slide" and slide[-4:]==".xml"):
                print(i+1, ":", slide)
                archivoSlide = os.path.join(rutaSlides, slide)
                with open(archivoSlide, "r", encoding="utf-8", errors="Ignore") as file:
                    texto = file.read()
                    print(texto)
                    print("_" * 50)
    else:
        print("El Archivo a descomprimir No es zip")
else:
    print("El dato ingresado No es un archivo")