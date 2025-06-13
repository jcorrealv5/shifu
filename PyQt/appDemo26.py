import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QTreeWidgetItem
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo26.ui", self)
        twCategoriaProducto = self.findChild(QtWidgets.QTreeWidget, "twCategoriaProducto")
        twCategoriaProducto.setHeaderLabels(["Codigo", "Nombre"])
        #Traer los datos de las Categorias y Productos
        archivoConfig=r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQtDemo19.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspCategoriaProductoListasCsv")
        if(data is not None):
            listas = data.split("_")
            listaCategorias = listas[0].split("¬")
            listaProductos = listas[1].split("¬")
            nCategorias = len(listaCategorias)
            nProductos = len(listaProductos)
            c=0
            pos=0
            for i in range(nCategorias):
                categorias = listaCategorias[i].split("|")
                nodoRaiz = QTreeWidgetItem()
                nodoRaiz.setText(0, categorias[0])
                nodoRaiz.setText(1, categorias[1])
                twCategoriaProducto.addTopLevelItem(nodoRaiz)
                for j in range(pos, nProductos):
                    c=c+1
                    productos = listaProductos[j].split("|")
                    if(productos[2]==categorias[0]):                        
                        nodoHijo = QTreeWidgetItem()
                        nodoHijo.setText(0, productos[0])
                        nodoHijo.setText(1, productos[1])
                        nodoRaiz.addChild(nodoHijo)
                    else:
                        pos = j
                        break
            print("Total de bucles: ", c)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())