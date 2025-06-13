import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMdiSubWindow
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, CustomTableViewModel, TableView, ComboBox

class ManProducto(QMdiSubWindow):
    def __init__(self, parent):
        super(ManProducto, self).__init__(parent)
        uic.loadUi("dlgDemo64_ManProducto.ui", self)
        
        #Obtener los controles de la GUI
        btnNuevo = self.findChild(QtWidgets.QPushButton, "btnNuevo")
        btnEditar = self.findChild(QtWidgets.QPushButton, "btnEditar")
        btnEliminar = self.findChild(QtWidgets.QPushButton, "btnEliminar")
        btnSalir = self.findChild(QtWidgets.QPushButton, "btnSalir")
        self.lblTotal = self.findChild(QtWidgets.QLabel, "lblTotal")
        self.tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        
        #Programar los eventos clicks de los Botones
        btnNuevo.clicked.connect(self.nuevoProducto)
        btnEditar.clicked.connect(self.editarProducto)
        btnEliminar.clicked.connect(self.eliminarProducto)
        btnSalir.clicked.connect(self.salir)
        
        #Conectar a Base de Datos para listar los productos
        archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\PyQtLog_Demo51.txt"
        self.con = clienteSQL(archivoConfig, archivoLog)
        data = self.con.EjecutarComandoCadena("uspProductoListas2Csv")
        if(data is not None):
            listas = data.split("_")
            self.listaProducto = listas[0].split("¬")
            self.listaProveedor = listas[1].split("¬")
            self.listaCategoria = listas[2].split("¬")
            #print("listaProducto\n", listaProducto)
            #print("\nlistaProveedor\n", listaProveedor)
            #print("\nlistaCategoria\n", listaCategoria)
            #Crear los anchos que vienen en la segunda fila de la lista
            self.anchos = self.listaProducto[1].split("|")
            self.llenarGrillaProductos(self.listaProducto)
        else:
            MessageBox.Show("Ocurrio un error al listar los productos")
            
    def llenarGrillaProductos(self, listaProductos):        
        #Crear un Modelo desde el origen de datos: lista
        self.modelo = CustomTableViewModel(listaProductos)
        #Enlazar el Modelo al Control QTableView
        self.tblProducto.setModel(self.modelo)
        #Ajustar los anchos de acuerdo al SP
        TableView.ConfigurarAnchos(self.tblProducto, self.anchos)
        #Mostrar el Total de registros desde el Modelo
        self.lblTotal.setText(str(self.modelo.rowCount()))
    
    def nuevoProducto(self):
        self.codigo = ""
        dlg = DialogoDetalle(self)
        dlg.exec()
        if (len(dlg.listaProducto)>0):
            self.llenarGrillaProductos(dlg.listaProducto)
        
    def editarProducto(self):
        fila = self.tblProducto.currentIndex().row()
        if(fila>-1):
            indice = self.modelo.index(fila,0)
            self.codigo = self.modelo.data(indice) 
            dlg = DialogoDetalle(self)
            dlg.exec()
            if (len(dlg.listaProducto)>0):
                self.llenarGrillaProductos(dlg.listaProducto)
        else:
            MessageBox.Show("Seleccione el Producto a Editar")
    
    def eliminarProducto(self):
        fila = self.tblProducto.currentIndex().row()
        if(fila>-1):
            indice = self.modelo.index(fila,0)
            codigo = str(self.modelo.data(indice))
            data = self.con.EjecutarComandoCadena("uspProductoEliminarCsv","ProductID",codigo, trx=True)
            if(data is not None):
                listaProducto = data.split("¬")
                self.llenarGrillaProductos(listaProducto)
                MessageBox.Show("Se elimino el Producto: " + codigo)
        else:
            MessageBox.Show("Seleccione el Producto a Eliminar")
        
    def salir(self):
        print("Salir")
        self.close()

class DialogoDetalle(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo51_Detalle.ui", self)
        #Obtener los Controles de la UI
        self.txtCodigo = self.findChild(QtWidgets.QLineEdit, "txtCodigo")
        self.txtNombre = self.findChild(QtWidgets.QLineEdit, "txtNombre")
        self.cboProveedor = self.findChild(QtWidgets.QComboBox, "cboProveedor")
        self.cboCategoria = self.findChild(QtWidgets.QComboBox, "cboCategoria")
        self.txtPrecioUnit = self.findChild(QtWidgets.QLineEdit, "txtPrecioUnit")
        self.txtStock = self.findChild(QtWidgets.QLineEdit, "txtStock")
        btnGrabar = self.findChild(QtWidgets.QPushButton, "btnGrabar")
        btnCancelar = self.findChild(QtWidgets.QPushButton, "btnCancelar")
        
        #Guardar variables globales del dialogo
        self.con = parent.con
        self.codigo = parent.codigo
        
        #Programar los eventos clicks de los botones
        btnGrabar.clicked.connect(self.grabarProducto)
        btnCancelar.clicked.connect(self.cancelar)
        #Llenar los 2 Combos con las listas
        ComboBox.LlenarDosCols(self.cboProveedor, parent.listaProveedor, primerItem="Seleccione")
        ComboBox.LlenarDosCols(self.cboCategoria, parent.listaCategoria, primerItem="Seleccione")
        if(self.codigo!=""):
            data = self.con.EjecutarComandoCadena("uspProductoObtenerPorId","ProductID", parent.codigo)
            if(data is not None):
                if(data!=""):
                    campos = data.split("|")
                    self.txtCodigo.setText(campos[0])
                    self.txtNombre.setText(campos[1])
                    self.cboProveedor.setCurrentText(campos[2])
                    self.cboCategoria.setCurrentText(campos[3])
                    self.txtPrecioUnit.setText(campos[4])
                    self.txtStock.setText(campos[5])
                else:
                    MessageBox.Show("No existe el producto: " + parent.codigo)
            else:
                MessageBox.Show("Ocurrio un error al obtener el producto: " + self.codigo)
        
    def grabarProducto(self):
        data = self.txtCodigo.text() + "|"
        data += self.txtNombre.text() + "|"
        proveedor = self.cboProveedor.itemData(self.cboProveedor.currentIndex())
        data += proveedor + "|"
        categoria = self.cboCategoria.itemData(self.cboCategoria.currentIndex())
        data += categoria + "|"
        data += self.txtPrecioUnit.text() + "|"
        data += self.txtStock.text()
        rpta = self.con.EjecutarComandoCadena("uspProductoGrabarCsv","Data", data, trx=True)
        self.listaProducto = []
        if(rpta is not None):
            if(rpta!=""):
                listas = rpta.split("_")
                self.listaProducto = listas[0].split("¬")
                codigo = listas[1]
                if(self.txtCodigo.text()==""):
                    MessageBox.Show("Se inserto el Producto: " + codigo)
                else:
                    MessageBox.Show("Se actualizo el Producto: " + codigo)
                self.close()
            else:
                MessageBox.Show("Ocurrio un error al grabar el producto: " + self.codigo)
        else:
            MessageBox.Show("Ocurrio un error al grabar el producto: " + self.codigo)
        
    def cancelar(self):
        print("Cancelando")
        self.close()