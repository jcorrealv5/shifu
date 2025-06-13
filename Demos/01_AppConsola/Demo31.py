import os, hashlib
#Demo 31: Hash usando hashlib.sha256()

print("Demo 31: Hash usando hashlib.sha256()")
archivo1 = input("Ingresa el archivo 1 a Resumir: ")
if(os.path.isfile(archivo1)):
    archivo2 = input("Ingresa el archivo 2 a Resumir: ")
    if(os.path.isfile(archivo2)):
        with open(archivo1,"rb") as file1:
            data1=file1.read()
        with open(archivo2,"rb") as file2:
            data2=file2.read()
        if(len(data1)==len(data2)):
            hash1 = hashlib.sha256()
            hash1.update(data1)
            valor1 = hash1.hexdigest()
            hash2 = hashlib.sha256()
            hash2.update(data2)
            valor2 = hash2.hexdigest()
            if(valor1==valor2):
                print("Los archivos son iguales: ", valor1)
            else:
                print(f"Los archivos son diferentes: hash1={valor1} y hash2={valor2}")
        else:
            print("Los archivos son de diferente tamanio")
    else:
        print("No existe el Archivo 2")
else:
    print("No existe el Archivo 1")