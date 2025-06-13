import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QStandardItemModel, QMovie
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modWindowsPyQt import MessageBox, TableView
from PyQt5.QtCore import QThread
from urllib.request import urlopen

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo67.ui", self)
        self.btnConsultarServicioWeb = self.findChild(QtWidgets.QPushButton, "btnConsultarServicioWeb")
        self.lblTotal = self.findChild(QtWidgets.QLabel, "lblTotal")
        self.tblProducto = self.findChild(QtWidgets.QTableView, "tblProducto")
        self.lblProgreso = self.findChild(QtWidgets.QLabel, "lblProgreso")
        self.btnConsultarServicioWeb.clicked.connect(self.consultarServicioWeb)
        self.lblProgreso.setVisible(False)
        self.hiloBD = None
        
    def consultarServicioWeb(self):
        if(self.btnConsultarServicioWeb.text()=="Consultar Servicio Web" and self.hiloBD is None):
            self.lblTotal.setText("")
            self.tblProducto.setVisible(False)
            self.lblProgreso.setVisible(True)
            archivoImagen = r"C:\Users\jhonf\Documents\Shifu\Iconos\Iconos\Progreso.gif"
            self.movie = QMovie(archivoImagen)
            self.lblProgreso.setMovie(self.movie)
            self.movie.start()
            self.btnConsultarServicioWeb.setText("Cancelar Consulta")
            self.hiloBD = WorkerWS(self)
            self.hiloBD.finalizado.connect(self.mostrarRptaFinal)
            self.hiloBD.start()
        else:
            self.hiloBD.terminate()
            self.tblProducto.setModel(None)
            self.iniciarPantalla()
    
    def iniciarPantalla(self):
        self.hiloBD = None
        self.btnConsultarServicioWeb.setText("Consultar Servicio Web")
        self.tblProducto.setVisible(True)
        self.movie.stop()
        self.lblProgreso.setVisible(False)
    
    def mostrarRptaFinal(self, rpta):
        self.iniciarPantalla()
        if(rpta!=""):
            cabeceras = "C1|C2|C3|Fecha|Monto1|Monto2|Flag|Concepto|Categoria"
            anchos = "80|80|80|80|80|80|80|200|200"
            listaCP = rpta.split("¬")
            listaCP.insert(0, anchos)
            listaCP.insert(0, cabeceras)
            modelo = QStandardItemModel()
            TableView.CrearTabla(listaCP, self.tblProducto, modelo)
            self.lblTotal.setText(str(modelo.rowCount()))
        else:
            MessageBox.Show("Ocurrio un error al llamar al Servicio Web")

class WorkerWS(QThread):
    finalizado = QtCore.pyqtSignal(str)
    
    def __init__(self, parent):
        super(WorkerWS, self).__init__(parent) 
    
    def run(self):
        #Aqui ejecutar el codigo que demora
        rpta = ""
        try:
            url = "https://sigazonaldesa.pvn.gob.pe:16443/Servicios/ListarComprobantePagoCSV/136"
            rptaHttp = urlopen(url)
            if(rptaHttp is not None):
                buffer = rptaHttp.read()
                rpta = buffer.decode("utf-8")
            self.finalizado.emit(rpta)
        except Exception as error:
            print("Error: ", str(error))

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())