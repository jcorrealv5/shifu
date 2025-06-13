import sys
sys.path.append("../00_Modulos")
from modUtilidades import beLog

print("Demo 47: Visualizando Atributos de un Objeto usando __dict__")

obeLog = beLog("Demo47", "Demo47")
obeLog.setLog("Metodo", "Error")

listaMiembros = obeLog.__dict__
print(listaMiembros)
print("Total de Atributos del Objeto: ", len(listaMiembros))

listaAtributos = obeLog.__dict__.keys()
print("Nombres de los Atributos")
print(listaAtributos)

print("Valores de los Atributos")
listaValores = obeLog.__dict__.values()
print(listaValores)
