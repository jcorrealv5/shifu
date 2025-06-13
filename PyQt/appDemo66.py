import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QStandardItemModel, QMovie
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import MessageBox, TableView
from PyQt5.QtCore import QThread

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo66.ui", self)
        self.btnConsultarProductosBD = self.findChild(QtWidgets.QPushButton, "btnConsultarProductosBD")
        self.lblTotal = self.findChild(QtWidgets.QLabel, "lblTotal")
        self.tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        self.lblProgreso = self.findChild(QtWidgets.QLabel, "lblProgreso")
        self.btnConsultarProductosBD.clicked.connect(self.consultarProductos)
        self.lblProgreso.setVisible(False)
        
    def consultarProductos(self):     
        self.tblProducto.setVisible(False)
        self.lblProgreso.setVisible(True)
        archivoImagen = r"C:\Users\jhonf\Documents\Shifu\Iconos\Iconos\Progreso.gif"
        self.movie = QMovie(archivoImagen)
        self.lblProgreso.setMovie(self.movie)
        self.movie.start()
        hiloBD = WorkerBD(self)
        hiloBD.finalizado.connect(self.mostrarRptaFinal)
        hiloBD.start()
    
    def mostrarRptaFinal(self, rpta):
        self.tblProducto.setVisible(True)
        self.movie.stop()
        self.lblProgreso.setVisible(False)
        if(rpta is not None):
            if(rpta!=""):
                listaProductos = rpta.split("¬")
                modelo = QStandardItemModel()
                TableView.CrearTabla(listaProductos, self.tblProducto, modelo)
                self.lblTotal.setText(str(modelo.rowCount()))
            else:
                MessageBox.Show("No hay registros en la tabla Productos")
        else:
            MessageBox.Show("Ocurrio un error al listar los Productos")

class WorkerBD(QThread):
    finalizado = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super(WorkerBD, self).__init__(parent) 
    
    def run(self):
        #Aqui ejecutar el codigo que demora
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        rpta = con.EjecutarComandoCadena("uspProductoListarDelayCsv")
        self.finalizado.emit(rpta) 

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())