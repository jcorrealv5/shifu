import os
#Demo19: Mantenimiento (CRUD) de Alumnos con Archivos de Texto
titulo = "Demo19: Mantenimiento (CRUD) de Alumnos con Archivos de Texto"
archivo = "Alumnos.txt"

def ListarAlumnos():
    lineas = []
    if(os.path.isfile(archivo)):
        with open(archivo, "r", encoding="utf-8") as file:
            data = file.read()
            lineas = data.split("\n")[:-1]
            lineas.sort()
    return lineas

def AgregarAlumno():
    alumno = input("Alumno a Agregar: ")
    alumnos = ListarAlumnos()
    if(alumno in alumnos):
        print("El alumno ya existe")
    else:
        with open(archivo, "a", encoding="utf-8") as file:
            file.write(alumno + "\n")
        print(f"El alumno {alumno} fue agregado")

def ActualizarAlumno():
    alumno = input("Alumno a Buscar: ")
    if(os.path.isfile(archivo)):
        with open(archivo, "r", encoding="utf-8") as fileR:
            data = fileR.read()
        existe=(data.find(alumno)>-1)
        if(existe):
            nuevoAlumno = input("Datos a Actualizar: ")
            with open(archivo, "w", encoding="utf-8") as fileW:
                data = data.replace(alumno, nuevoAlumno)
                fileW.write(data)
            print(f"El alumno {alumno} fue actualizado por {nuevoAlumno}")
        else:
            print("Alumno No existe en el Archivo")

def EliminarAlumno():
    alumno = input("Alumno a Eliminar: ")
    if(os.path.isfile(archivo)):
        with open(archivo, "r", encoding="utf-8") as fileR:
            data = fileR.read()
        existe=(data.find(alumno)>-1)
        if(existe):
            with open(archivo, "w", encoding="utf-8") as fileW:
                data = data.replace(alumno + "\n", "")
                fileW.write(data)
            print(f"El alumno {alumno} fue eliminado")
        else:
            print("Alumno No existe en el Archivo")

while True:
    print("\n")
    print(titulo)
    print("1. Listado de Alumnos Ordenados")
    print("2. Agregar un Nuevo Alumnos")
    print("3. Actualizar los datos del Alumno")
    print("4. Eliminar el Alumno")
    print("5. Salir de la Aplicacion")
    opcion = input("Ingresa un digito del 1 al 5: ")    
    if(opcion in ["1","2","3","4","5"]):
        if(opcion=="1"):
            alumnos = ListarAlumnos()
            print(alumnos)
        if(opcion=="2"):
            AgregarAlumno()
        if(opcion=="3"):
            ActualizarAlumno()
        if(opcion=="4"):
            EliminarAlumno()
        if(opcion=="5"):
            break