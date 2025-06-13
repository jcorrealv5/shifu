import sys, re
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, TableView, CustomTableViewModel, SortFilterProxyModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo49.ui", self)
        #Obtener los controles de la GUI
        tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        self.lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        self.txtValor = self.findChild(QtWidgets.QLineEdit, "txtValor")
        btnFiltrar = self.findChild(QtWidgets.QPushButton, "btnFiltrar")
        self.cboCampo = self.findChild(QtWidgets.QComboBox, "cboCampo")
        self.cboOperador = self.findChild(QtWidgets.QComboBox, "cboOperador")
        
        #Programar el Boton Filtrar
        btnFiltrar.clicked.connect(self.filtrarPorNombre)
        #Programar el Combo de Campo para llenar el Combo de Operador
        self.cboCampo.currentIndexChanged.connect(self.cambiarOperador)
        
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
                #Obtener los tipos de datos de la tabla
                self.tipos = listaProductos[2].split("|")
                #Crear el Modelo desde el origen de datos
                modelo = CustomTableViewModel(listaProductos, esFloat=True)
                #Crear el Intermediario de datos
                self.proxy = SortFilterProxyModel(self)
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
        tipo = self.tipos[col]
        operador = self.cboOperador.currentIndex()        
        if(tipo=="int" or tipo=="float"):
            if(texto==""):
                self.proxy.setFilterKeyColumn(col)
                self.proxy.setValueOperator("N", operador, "")
            else:                    
                if(tipo=="int"):
                    if(texto.isnumeric()):
                        valor = int(texto)
                        self.proxy.setFilterKeyColumn(col)
                        self.proxy.setValueOperator("N", operador, valor)
                    else:
                        MessageBox.Show("El dato debe ser entero")
                        self.txtValor.setText("")
                elif(tipo=="float"):
                    if(bool(re.fullmatch(r'-?\d+(\.\d+)?', texto))):
                        valor = float(texto)
                        self.proxy.setFilterKeyColumn(col)
                        self.proxy.setValueOperator("N", operador, valor)
                    else:
                        MessageBox.Show("El dato debe ser float")
                        self.txtValor.setText("")
        else:
            self.proxy.setFilterKeyColumn(col)
            self.proxy.setValueOperator("S", operador, texto)
        #Mostrar el Total de registros
        self.lblTotalRegistros.setText(str(self.proxy.rowCount()))
    
    def cambiarOperador(self, indice):
        tipo = self.tipos[indice]
        if(tipo=="int" or tipo=="float"):
            operadores = ["=", ">", "<", ">=", "<=", "<>"]
        else:
            operadores = ["Inicia", "Termina", "Contiene"]
        #Llenar el Combo de Operadores
        self.cboOperador.clear()
        self.cboOperador.addItems(operadores)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())