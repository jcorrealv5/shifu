import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtCore import QThread

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo68.ui", self)
        
        self.txtArchivo = self.findChild(QtWidgets.QLineEdit, "txtArchivo")
        btnSeleccionarArchivo = self.findChild(QtWidgets.QPushButton, "btnSeleccionarArchivo")
        btnProcesar = self.findChild(QtWidgets.QPushButton, "btnProcesar")
        self.lstResultado = self.findChild(QtWidgets.QListWidget, "lstResultado")
        self.pbrArchivo = self.findChild(QtWidgets.QProgressBar, "pbrArchivo")
        self.lblTotal = self.findChild(QtWidgets.QLabel, "lblTotal")
        
        btnSeleccionarArchivo.clicked.connect(self.seleccionarArchivo)
        btnProcesar.clicked.connect(self.procesarArchivo)

    def seleccionarArchivo(self):
        dlg = QFileDialog()
        dlg.exec()
        self.Archivo = dlg.selectedFiles()[0]
        self.txtArchivo.setText(self.Archivo)
    
    def procesarArchivo(self):
        hiloContarLineas = WorkerContarLineas(self)
        hiloContarLineas.finalizado.connect(self.mostrarRptaContarLineas)
        hiloContarLineas.start()
    
    def mostrarRptaContarLineas(self, nLineas):
        self.TotalLineas = nLineas
        hiloEstadisticas = WorkerEstadisticas(self)
        hiloEstadisticas.progreso.connect(self.mostrarProgresoEstadisticas)
        hiloEstadisticas.estadistica.connect(self.mostrarProcesoEstadistica)
        hiloEstadisticas.finalizado.connect(self.mostrarRptaEstadisticas)
        hiloEstadisticas.start()
    
    def mostrarProgresoEstadisticas(self, n):
        self.pbrArchivo.setValue(n)
    
    def mostrarProcesoEstadistica(self, rpta):
        self.lstResultado.addItem(rpta)
    
    def mostrarRptaEstadisticas(self):
        self.lblTotal.setText(str(self.lstResultado.count()) + " / " + str(self.TotalLineas))

class WorkerContarLineas(QThread):
    finalizado = QtCore.pyqtSignal(int)
    
    def __init__(self, parent):
        super(WorkerContarLineas, self).__init__(parent) 
        self.Archivo = parent.Archivo
    
    def run(self):
        #Aqui ejecutar el codigo que demora
        c = 0
        with open(self.Archivo, "r", encoding="utf-8") as file:
            for linea in file:
                c = c + 1
        self.finalizado.emit(c)
    
class WorkerEstadisticas(QThread):
    finalizado = QtCore.pyqtSignal()
    progreso = QtCore.pyqtSignal(int)
    estadistica = QtCore.pyqtSignal(str)
        
    def __init__(self, parent):
        super(WorkerEstadisticas, self).__init__(parent) 
        self.Archivo = parent.Archivo
        self.TotalLineas = parent.TotalLineas
    
    def run(self):
        bloque = int(self.TotalLineas / 100)
        #Aqui ejecutar el codigo que demora
        c = 0
        x = 0
        with open(self.Archivo, "r", encoding="utf-8") as file:            
            campos = file.readline().split("|")
            nroSerieUltimo = campos[0] + "-" +campos[1] + "-" + campos[3]
        debe = 0
        haber = 0
        with open(self.Archivo, "r", encoding="utf-8") as file:
            for linea in file:
                campos = linea.split("|")
                nroSerie = campos[0] + "-" +campos[1] + "-" + campos[3]
                if(nroSerie!=nroSerieUltimo):
                    self.estadistica.emit(str(nroSerieUltimo + ", Debe=" + str(debe) + ", Haber=" + str(haber))) 
                    debe = float(campos[17])
                    haber = float(campos[18])
                else:
                    debe += float(campos[17])
                    haber += float(campos[18])
                nroSerieUltimo = nroSerie
                c = c + 1
                if(c % bloque==0):
                    x = x + 1
                    self.progreso.emit(x)
        self.finalizado.emit() 

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())