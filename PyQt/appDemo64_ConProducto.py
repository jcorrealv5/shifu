import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtWidgets import QMdiSubWindow
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, TableView, CustomTableViewModel, EditableHeaderView

class ConProducto(QMdiSubWindow):
    def __init__(self, parent):
        super(ConProducto, self).__init__(parent)
        uic.loadUi("dlgDemo64_ConProducto.ui", self)
        #Obtener los controles de la GUI
        tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        self.lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        #Acceso a Datos
        archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\PyQtDemo46.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProductoListasCsv")
        if(data is not None):
            if(data!=""):
                listas = data.split("_")
                #Crear el origen de datos: list<str>
                listaProductos = listas[0].split("¬")
                listaProveedores = listas[1].split("¬")
                listaCategorias = listas[2].split("¬")
                combosIndices = [2,3]
                combosListas = []
                combosListas.append(listaProveedores)
                combosListas.append(listaCategorias)
                #Obtener los anchos de la tabla
                anchos = listaProductos[1].split("|")
                #Crear el Modelo desde el origen de datos
                modelo = CustomTableViewModel(listaProductos, esFloat=True)
                #Crear el Intermediario de datos
                self.proxy = QSortFilterProxyModel(self)
                self.proxy.setSourceModel(modelo)
                #Configurar la Cabecera del QTableView 
                cabEditable = EditableHeaderView(tblProducto, combosIndices, combosListas)
                cabEditable.textChanged.connect(self.filtrarColumna)
                tblProducto.setHorizontalHeader(cabEditable)
                #Enlazar el proxy al Control: QTableView
                tblProducto.setModel(self.proxy)
                #Configurar anchos
                TableView.ConfigurarAnchos(tblProducto, anchos)
                #Configurar la Ordenacion en el Control
                #tblProducto.setSortingEnabled(True)
                #tblProducto.sortByColumn(0, Qt.AscendingOrder)
                #Mostrar el Total de registros
                self.lblTotalRegistros.setText(str(self.proxy.rowCount()))
            else:
                MessageBox.Show("No existe registros en Productos")
        else:
            MessageBox.Show("Ocurrio un Error al listar los Productos")
    
    def filtrarColumna(self, col, texto):
        self.proxy.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy.setFilterKeyColumn(col)
        self.proxy.setFilterWildcard("*{0}*".format(texto) if texto!="" else "")
        #Mostrar el Total de registros
        self.lblTotalRegistros.setText(str(self.proxy.rowCount()))