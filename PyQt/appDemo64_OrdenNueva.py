import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMdiSubWindow
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, CustomTableViewModel, TableView
from datetime import datetime

#Conectar a la BD y obtener las ordenes
archivoConfig = r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
archivoLog = r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQt_Demo53.txt"

class OrdenNueva(QMdiSubWindow):
    def __init__(self, parent):
        super(OrdenNueva, self).__init__(parent)
        uic.loadUi("dlgDemo64_Orden.ui", self)
        #Obtener los controles de la GUI
        btnNuevo = self.findChild(QtWidgets.QPushButton, "btnNuevo")
        btnEditar = self.findChild(QtWidgets.QPushButton, "btnEditar")
        btnSalir = self.findChild(QtWidgets.QPushButton, "btnSalir")
        lblTotal = self.findChild(QtWidgets.QLabel, "lblTotal")
        self.tblOrden = self.findChild(QtWidgets.QTableView, "tblOrden")
        
        #Programar Eventos Clicks de Botones
        btnNuevo.clicked.connect(self.nuevaOrden)
        btnEditar.clicked.connect(self.editarOrden)
        btnSalir.clicked.connect(self.salir)
        
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspOrdenListasCsv")
        if(data is not None):
            if(data!=""):
                listas = data.split("_")
                listaOrdenes = listas[0].split(";")
                self.listaClientes = listas[1].split(";")
                self.listaEmpleados = listas[2].split(";")
                anchos = listaOrdenes[1].split("|")
                self.modelo = CustomTableViewModel(listaOrdenes)
                self.tblOrden.setModel(self.modelo)
                TableView.ConfigurarAnchos(self.tblOrden, anchos)
                lblTotal.setText(str(self.modelo.rowCount()))
            else:
                MessageBox.Show("No hay registros de Ordenes")
        else:
            MessageBox.Show("Ocurrio un Error al Obtener las Ordenes")

    def nuevaOrden(self):
        self.nroOrden = ""
        dlg = DialogoDetalle(self)
        dlg.exec()
    
    def editarOrden(self):
        fila = self.tblOrden.currentIndex().row()
        if(fila>-1):
            self.nroOrden = str(self.modelo.data(self.modelo.index(fila,0)))
            dlg = DialogoDetalle(self)
            dlg.exec()
        else:
            MessageBox.Show("Selecciona la Orden a Mostrar")
    
    def salir(self):
        self.close()

class DialogoDetalle(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.listaClientes = parent.listaClientes
        self.listaEmpleados = parent.listaEmpleados
        self.nroOrden = parent.nroOrden
        
        uic.loadUi("dlgDemo64_Detalle.ui", self)
        
        #Obtener los controles de la GUI
        self.txtNroOrden = self.findChild(QtWidgets.QLineEdit, "txtNroOrden")
        self.txtFechaOrden = self.findChild(QtWidgets.QDateEdit, "txtFechaOrden")
        self.txtNombreCliente = self.findChild(QtWidgets.QLineEdit, "txtNombreCliente")
        btnAyudaCliente = self.findChild(QtWidgets.QPushButton, "btnAyudaCliente")
        self.txtNombreEmpleado = self.findChild(QtWidgets.QLineEdit, "txtNombreEmpleado")
        btnAyudaEmpleado = self.findChild(QtWidgets.QPushButton, "btnAyudaEmpleado")
        btnGrabarOrden = self.findChild(QtWidgets.QPushButton, "btnGrabarOrden")
        self.btnNuevo = self.findChild(QtWidgets.QPushButton, "btnNuevo")
        self.btnEditar = self.findChild(QtWidgets.QPushButton, "btnEditar")
        self.btnEliminar = self.findChild(QtWidgets.QPushButton, "btnEliminar")
        self.tblDetalle = self.findChild(QtWidgets.QTableView, "tblDetalle")
        
        #Configurar para que la fecha sea la actual
        self.txtFechaOrden.setDate(datetime.now())
        
        #Programar Eventos Clicks de Botones
        btnAyudaCliente.clicked.connect(self.mostrarAyudaCliente)
        btnAyudaEmpleado.clicked.connect(self.mostrarAyudaEmpleado)
        btnGrabarOrden.clicked.connect(self.grabarOrden)
        self.btnNuevo.clicked.connect(self.nuevoDetalle)
        self.btnEditar.clicked.connect(self.editarDetalle)
        self.btnEliminar.clicked.connect(self.eliminarDetalle)
        
        #Ocultar los Botones de Detalles
        self.mostrarBotonesDetalle(False)
        
        if(self.nroOrden!=""):
            con = clienteSQL(archivoConfig, archivoLog)
            data = con.EjecutarComandoCadena("uspOrdenObtenerPorIdCsv","OrderID",self.nroOrden)
            if(data is not None):
                listas = data.split("_")
                camposOrden = listas[0].split("|")
                self.txtNroOrden.setText(self.nroOrden)
                #self.txtFechaOrden.setDate(camposOrden[0])                
                self.codEmpleado = camposOrden[1]
                self.txtNombreEmpleado.setText(camposOrden[2])
                self.codCliente = camposOrden[3]
                self.txtNombreCliente.setText(camposOrden[4])
                listaDetalle = listas[1].split(";")                
                self.mostrarBotonesDetalle(True)
                self.mostrarDetalles(listaDetalle)
    
    def mostrarDetalles(self, listaDetalle):
        anchos = listaDetalle[1].split("|")                
        self.modelo = CustomTableViewModel(listaDetalle, colsSubtotales = [3,4,5], textoSubtotales={"2":"Total de la Orden"})
        self.tblDetalle.setModel(self.modelo)
        TableView.ConfigurarAnchos(self.tblDetalle, anchos)
    
    def mostrarBotonesDetalle(self, visible):
        self.btnNuevo.setVisible(visible)
        self.btnEditar.setVisible(visible)
        self.btnEliminar.setVisible(visible)

    def mostrarAyudaCliente(self):
        dlg = DialogoAyuda(self.listaClientes, "Clientes")
        dlg.exec()
        if(dlg.data is not None):
            campos = dlg.data.split("|")
            self.codCliente = campos[0]
            self.txtNombreCliente.setText(campos[1])

    def mostrarAyudaEmpleado(self):
        dlg = DialogoAyuda(self.listaEmpleados, "Empleados")
        dlg.exec()
        if(dlg.data is not None):
            campos = dlg.data.split("|")
            self.codEmpleado = campos[0]
            self.txtNombreEmpleado.setText(campos[1])
    
    def grabarOrden(self):
        if(self.txtNombreCliente.text()!=""):
            if(self.txtNombreEmpleado.text()!=""):
                data = self.txtNroOrden.text() + "|" + self.txtFechaOrden.date().toString("dd-MM-yyyy")
                data += "|" + self.codCliente + "|" + self.codEmpleado
                con = clienteSQL(archivoConfig, archivoLog)
                self.nroOrden = con.EjecutarComandoCadena("uspOrdenGrabarCsv", "Data", data, trx=True)
                if(self.nroOrden is not None):
                    self.txtNroOrden.setText(self.nroOrden)
                    #Mostrar los Botones de Detalles
                    self.mostrarBotonesDetalle(True)
                    MessageBox.Show("Se grabo correctamente la orden")
                else:
                    MessageBox.Show("Ocurrio un error al grabar la orden")
            else:
                MessageBox.Show("Selecciona un Empleado a grabar la orden")
        else:
            MessageBox.Show("Selecciona un Cliente a grabar la orden")

    def nuevoDetalle(self):
        dlg = DialogoProducto(self.nroOrden, "")
        dlg.exec()
        if(dlg.listaDetalle is not None):
            self.mostrarDetalles(dlg.listaDetalle)
    
    def editarDetalle(self):
        fila = self.tblDetalle.currentIndex().row()
        if(fila>-1):
            idDetalle = str(self.modelo.data(self.modelo.index(fila,0)))
            dlg = DialogoProducto(self.nroOrden, idDetalle)
            dlg.exec()
            if(dlg.listaDetalle is not None):
                self.mostrarDetalles(dlg.listaDetalle)
        else:
            MessageBox.Show("Selecciona el Detalle del Producto a Mostrar")
    
    def eliminarDetalle(self):
        pass

class DialogoAyuda(QDialog):
    def __init__(self, listaAyuda, nombreAyuda):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo64_Ayuda.ui", self)
        #Obtener los controles de la GUI
        self.tblAyuda = self.findChild(QtWidgets.QTableView, "tblAyuda")
        btnSeleccionar = self.findChild(QtWidgets.QPushButton, "btnSeleccionar")
        #Mostrar la Ayuda
        anchos = listaAyuda[1].split("|")
        self.modelo = CustomTableViewModel(listaAyuda)
        self.tblAyuda.setModel(self.modelo)
        TableView.ConfigurarAnchos(self.tblAyuda, anchos)
        self.setWindowTitle("Ayuda de " + nombreAyuda)
        #Programar el evento click del unico Boton
        btnSeleccionar.clicked.connect(self.seleccionarRegistro)
        self.data = None
    
    def seleccionarRegistro(self):
        fila = self.tblAyuda.currentIndex().row()
        if(fila>-1):
            cols = self.modelo.columnCount()
            self.data = ""
            for i in range(cols):
                self.data += str(self.modelo.data(self.modelo.index(fila,i)))
                if(i<cols-1):
                    self.data += "|"
            self.close()
        else:
            MessageBox.Show("Seleccione el Registro a Mostrar")

class DialogoProducto(QDialog):
    def __init__(self, idOrden, idDetalle):
        QDialog.__init__(self)
        self.idOrden = idOrden
        self.idDetalle = idDetalle
        
        uic.loadUi("dlgDemo53_Producto.ui", self)
        #Obtener los controles de la GUI
        self.txtNombreProducto = self.findChild(QtWidgets.QLineEdit, "txtNombreProducto")
        btnAyudaProducto = self.findChild(QtWidgets.QPushButton, "btnAyudaProducto")
        self.txtPrecioUnitario = self.findChild(QtWidgets.QDoubleSpinBox, "txtPrecioUnitario")
        self.txtCantidad = self.findChild(QtWidgets.QSpinBox, "txtCantidad")
        self.txtPrecioTotal = self.findChild(QtWidgets.QLineEdit, "txtPrecioTotal")
        btnGrabar = self.findChild(QtWidgets.QPushButton, "btnGrabar")
        
        #Programar los eventos clicks de los Botones
        btnAyudaProducto.clicked.connect(self.mostrarAyudaProducto)
        btnGrabar.clicked.connect(self.grabarDetalle)
        #Programar los Cambios de los Controles Numericos (SpinBoxs)
        self.txtPrecioUnitario.valueChanged.connect(self.calcularPrecioTotal)
        self.txtCantidad.valueChanged.connect(self.calcularPrecioTotal)
        
        self.listaDetalle = None
        if(self.idDetalle!=""):
            con = clienteSQL(archivoConfig, archivoLog)
            data = con.EjecutarComandoCadena("uspDetalleObtenerPorId","IdDetalle",self.idDetalle)
            if(data is not None):
                if(data!=""):
                    camposDetalle = data.split("|")
                    self.idProducto = camposDetalle[0]
                    self.txtNombreProducto.setText(str(camposDetalle[1]))
                    self.txtPrecioUnitario.setValue(float(camposDetalle[2]))
                    self.txtCantidad.setValue(int(camposDetalle[3]))
                    self.txtPrecioTotal.setText(camposDetalle[4])
                    self.txtCantidad.setMaximum(int(camposDetalle[5]))
        
    def mostrarAyudaProducto(self):
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProductoListar2Csv")
        if(data is not None):
            if(data!=""):
                self.listaProductos = data.split(";")
                dlg = DialogoAyuda(self.listaProductos, "Productos")
                dlg.exec()
                if(dlg.data is not None):
                    campos = dlg.data.split("|")
                    self.idProducto = campos[0]
                    self.txtNombreProducto.setText(campos[1])
                    self.txtPrecioUnitario.setValue(float(campos[2]))
                    self.txtCantidad.setMaximum(int(campos[3]))
            else:
                MessageBox.Show("No hay registros de Ordenes")
        else:
            MessageBox.Show("Ocurrio un Error al Obtener las Ordenes")
    
    def calcularPrecioTotal(self, value):
        precioTotal = self.txtPrecioUnitario.value() * self.txtCantidad.value()
        self.txtPrecioTotal.setText(str(precioTotal))
    
    def grabarDetalle(self):
        if(self.txtNombreProducto.text()!=""):
            data = self.idDetalle + "|" + self.idOrden
            data += "|" + self.idProducto + "|" 
            data += str(self.txtPrecioUnitario.value()) + "|" 
            data += str(self.txtCantidad.value())
            con = clienteSQL(archivoConfig, archivoLog)
            rpta = con.EjecutarComandoCadena("uspDetalleGrabarCsv", "Data", data, trx=True)
            if(rpta is not None):
                self.listaDetalle = rpta.split(";")
                MessageBox.Show("Se grabo correctamente el detalle")
                self.close()
            else:
                MessageBox.Show("Ocurrio un error al grabar el detalle")
        else:
            MessageBox.Show("Selecciona el Producto a grabar el detalle")