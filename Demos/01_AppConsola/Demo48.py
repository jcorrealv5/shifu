import sys, inspect
sys.path.append("../00_Modulos")
from modUtilidades import beLog

print("Demo 48: Visualizando Miembros de un Objeto usando inspect")

obeLog = beLog("Demo47", "Demo47")
obeLog.setLog("Metodo", "Error")

listaMiembros = inspect.getmembers(obeLog)
ca = 0
cm = 0
for miembro in listaMiembros:
  if not miembro[0].startswith('_'):
    if not inspect.ismethod(miembro[1]): 
        ca=ca+1
        print("Atributo " + str(ca) + ": " + miembro[0] + " = " + miembro[1])
    else:
        cm=cm+1
        print("Metodo " + str(cm) + ": " + miembro[0])