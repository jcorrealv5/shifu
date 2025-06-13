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
        uic.loadUi("dlgDemo48.ui", self)
        #Obtener los controles de la GUI
        tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        self.lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        self.txtValor = self.findChild(QtWidgets.QLineEdit, "txtValor")
        btnFiltrar = self.findChild(QtWidgets.QPushButton, "btnFiltrar")
        self.cboCampo = self.findChild(QtWidgets.QComboBox, "cboCampo")
        
        #Programar el Boton Filtrar
        btnFiltrar.clicked.connect(self.filtrarPorNombre)
        
        #Acceso a Datos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProductoListarCsv")
        if(data is not None):
            if(data!=""):
                #Crear el origen de datos: list<str>
                listaProductos = data.split("¬")
                #Obtener los campos de la tabla
                campos = listaProductos[0].split("|")
                #Obtener los anchos de la tabla
                anchos = listaProductos[1].split("|")
                #Crear el Modelo desde el origen de datos
                modelo = CustomTableViewModel(listaProductos, esFloat=True)
                #Crear el Intermediario de datos
                self.proxy = QSortFilterProxyModel(self)
                self.proxy.setSourceModel(modelo)
                #Enlazar el proxy al Control: QTableView
                tblProducto.setModel(self.proxy)
                #Configurar anchos
                TableView.ConfigurarAnchos(tblProducto, anchos)
                #Configurar la Ordenacion en el Control
                tblProducto.setSortingEnabled(True)
                tblProducto.sortByColumn(0, Qt.AscendingOrder)
                #Mostrar el Total de registros
                self.lblTotalRegistros.setText(str(self.proxy.rowCount()))
                #Llenar el Combo de Campos
                self.cboCampo.addItems(campos)
            else:
                MessageBox.Show("No existe registros en Productos")
        else:
            MessageBox.Show("Ocurrio un Error al listar los Productos")

    def filtrarPorNombre(self):
        col = self.cboCampo.currentIndex()
        texto = self.txtValor.text()
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy.setFilterKeyColumn(col)
        self.proxy.setFilterWildcard("*{0}*".format(texto) if texto!="" else "")
        #Mostrar el Total de registros
        self.lblTotalRegistros.setText(str(self.proxy.rowCount()))

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())