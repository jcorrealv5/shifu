import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QComboBox, QPushButton
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, CustomTableViewModel, TableView

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo52.ui", self)
        
        #Obtener los controles de la GUI
        btnNuevo = self.findChild(QtWidgets.QPushButton, "btnNuevo")
        btnSalir = self.findChild(QtWidgets.QPushButton, "btnSalir")
        self.lblTotal = self.findChild(QtWidgets.QLabel, "lblTotal")
        self.tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        
        #Programar los eventos clicks de los Botones
        btnNuevo.clicked.connect(self.nuevoProducto)
        btnSalir.clicked.connect(self.salir)
        
        #Conectar a Base de Datos para listar los productos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        self.con = clienteSQL(archivoConfig, archivoLog)
        data = self.con.EjecutarComandoCadena("uspProductoListasCboCsv")
        if(data is not None):
            listas = data.split("_")
            self.listaProducto = listas[0].split("¬")
            self.listaProveedor = listas[1].split("¬")
            self.listaCategoria = listas[2].split("¬")
            #Crear los anchos que vienen en la segunda fila de la lista
            self.anchos = self.listaProducto[1].split("|")
            self.llenarGrillaProductos(self.listaProducto)            
    
    def llenarGrillaProductos(self, listaProductos):        
        #Crear un Modelo desde el origen de datos: lista
        self.modelo = CustomTableViewModel(listaProductos, soloLectura=False, numColsExtras=2)
        #Enlazar el Modelo al Control QTableView
        self.tblProducto.setModel(self.modelo)
        #Ajustar los anchos de acuerdo al SP
        TableView.ConfigurarAnchos(self.tblProducto, self.anchos)
        #Mostrar el Total de registros desde el Modelo
        self.lblTotal.setText(str(self.modelo.rowCount()))
        #Agregar Combos a las 2 Columnas
        nRegistros = self.modelo.rowCount()
        nProveedores = len(self.listaProveedor)
        nCategorias = len(self.listaCategoria)
        nCols = self.modelo.columnCount()
        for i in range(nRegistros):
            #LLenar los Combos de Proveedores
            cboProv = QComboBox()
            for j in range(nProveedores):
                camposProv = self.listaProveedor[j].split("|")
                cboProv.addItem(camposProv[1], camposProv[0])
            indiceProv = self.modelo.index(i,2)
            nombreProv = self.modelo.data(indiceProv)
            cboProv.setCurrentText(nombreProv)
            self.tblProducto.setIndexWidget(self.modelo.index(i, 2), cboProv)
            #LLenar los Combos de Categorias
            cboCat = QComboBox()
            for j in range(nCategorias):
                camposCat = self.listaCategoria[j].split("|")
                cboCat.addItem(camposCat[1], camposCat[0])
            indiceCat = self.modelo.index(i,3)
            nombreCat = self.modelo.data(indiceCat)
            cboCat.setCurrentText(nombreCat)
            self.tblProducto.setIndexWidget(self.modelo.index(i, 3), cboCat)
            #Crear una Columna para los Botones de Grabar
            btnGrabar = QPushButton()
            btnGrabar.setText("Grabar")
            btnGrabar.clicked.connect(self.grabarProducto)
            self.tblProducto.setIndexWidget(self.modelo.index(i, nCols-2), btnGrabar)
            #Crear una Columna para los Botones de Eliminar
            btnEliminar = QPushButton()
            btnEliminar.setText("Eliminar")
            btnEliminar.clicked.connect(self.eliminarProducto)
            self.tblProducto.setIndexWidget(self.modelo.index(i, nCols-1), btnEliminar)
    
    def nuevoProducto(self):        
        indice = self.modelo.index(self.modelo.rowCount(),0)
        self.modelo.insertRow(self.modelo.rowCount(), indice)        
    
    def grabarProducto(self):
        fila = self.tblProducto.currentIndex().row()
        indiceCodigo = self.modelo.index(fila,0)
        codigo = str(self.modelo.data(indiceCodigo))
        indiceNombre = self.modelo.index(fila,1)
        nombre = str(self.modelo.data(indiceNombre))
        indiceProv = self.modelo.index(fila,2)
        comboProv = self.tblProducto.indexWidget(indiceProv)
        idProv = comboProv.currentData()
        indiceCat = self.modelo.index(fila,3)
        comboCat = self.tblProducto.indexWidget(indiceCat)
        idCat = comboCat.currentData()
        indicePrecio = self.modelo.index(fila,4)
        precio = str(self.modelo.data(indicePrecio))
        indiceStock = self.modelo.index(fila,5)
        stock = str(self.modelo.data(indiceStock))
        data = codigo + "|" + nombre + "|" + idProv + "|" + idCat + "|" + precio + "|" + stock
        rpta = self.con.EjecutarComandoCadena("uspProductoGrabar2Csv","Data", data, trx=True)
        if(rpta is not None):
            if(rpta!=""):
                if(codigo=="0"):
                    MessageBox.Show("Se inserto el Producto: " + rpta)
                else:
                    MessageBox.Show("Se actualizo el Producto: " + rpta)
    
    def eliminarProducto(self):
        fila = self.tblProducto.currentIndex().row()
        indice = self.modelo.index(fila,0)
        codigo = str(self.modelo.data(indice))
        data = self.con.EjecutarComandoCadena("uspProductoEliminar2Csv","ProductID",codigo, trx=True)
        if(data is not None):
            listaProducto = data.split("¬")
            self.llenarGrillaProductos(listaProducto)
            MessageBox.Show("Se elimino el Producto: " + codigo)
    
    def salir(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())