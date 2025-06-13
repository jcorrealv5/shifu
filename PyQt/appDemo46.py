import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, TableView, CustomTableViewModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo46.ui", self)
        #Obtener los controles de la GUI
        tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        #Acceso a Datos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProductoListarCsv")
        if(data is not None):
            if(data!=""):
                #Crear el origen de datos: list<str>
                listaProductos = data.split("¬")
                #Obtener los anchos de la tabla
                anchos = listaProductos[1].split("|")
                #Crear el Modelo desde el origen de datos
                modelo = CustomTableViewModel(listaProductos, esFloat=True)
                #Crear el Intermediario de datos
                proxy = QSortFilterProxyModel(self)
                proxy.setSourceModel(modelo)
                #Enlazar el proxy al Control: QTableView
                tblProducto.setModel(proxy)
                #Configurar anchos
                TableView.ConfigurarAnchos(tblProducto, anchos)
                #Configurar la Ordenacion en el Control
                tblProducto.setSortingEnabled(True)
                tblProducto.sortByColumn(0, Qt.AscendingOrder)
                #Mostrar el Total de registros
                lblTotalRegistros.setText(str(proxy.rowCount()))
            else:
                MessageBox.Show("No existe registros en Productos")
        else:
            MessageBox.Show("Ocurrio un Error al listar los Productos")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())