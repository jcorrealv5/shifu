import sys
sys.path.append("../00_Modulos")
from modUtilidades import beLog

print("Demo 46: Visualizando Miembros de una Clase y un Objeto usando dir")

listaMiembrosClase = dir(beLog)
print(listaMiembrosClase)
print("Total de Miembros de la Clase: ", len(listaMiembrosClase))

obeLog = beLog("Demo46", "Demo46")
obeLog.setLog("Metodo", "Sin Error")
listaMiembrosObjeto = dir(obeLog)
nLista = len(listaMiembrosObjeto)
print(listaMiembrosObjeto)
print("Total de Miembros del Objeto: ", nLista)

for miembro in listaMiembrosObjeto:
    if(not miembro.startswith("_")):
        print(miembro)