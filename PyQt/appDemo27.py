import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import TreeWidget

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo27.ui", self)
        twProveedorProducto = self.findChild(QtWidgets.QTreeWidget, "twProveedorProducto")
        twProveedorProducto.setHeaderLabels(["Codigo", "Nombre"])
        #Traer los datos de las Categorias y Productos
        archivoConfig=r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQtDemo19.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspProveedorProductoListasCsv")
        if(data is not None):
            listas = data.split("_")
            listaProveedores = listas[0].split("¬")
            listaProductos = listas[1].split("¬")
            TreeWidget.LlenarCon2Listas(twProveedorProducto, listaProveedores, listaProductos, 2, True)            

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())