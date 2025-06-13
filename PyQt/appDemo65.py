import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modWindowsPyQt import MessageBox
from PyQt5.QtCore import QThread

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo65.ui", self)
        self.txtNumBucles = self.findChild(QtWidgets.QSpinBox, "txtNumBucles")
        self.btnEjecutarBucles = self.findChild(QtWidgets.QPushButton, "btnEjecutarBucles")
        self.pbrBucles = self.findChild(QtWidgets.QProgressBar, "pbrBucles")
        btnCancelarThread = self.findChild(QtWidgets.QPushButton, "btnCancelarThread")        
        self.hilo = None
        
        self.btnEjecutarBucles.clicked.connect(self.ejecutarBucles)
        btnCancelarThread.clicked.connect(self.cancelarThread)
        
    def ejecutarBucles(self):
        self.pbrBucles.setValue(0)
        self.btnEjecutarBucles.setEnabled(False)
        self.numBucles = self.txtNumBucles.value()
        self.hilo = WorkerBucles(self)
        self.hilo.progreso.connect(self.mostrarProgreso)
        self.hilo.finalizado.connect(self.mostrarRptaFinal)
        self.hilo.start()
    
    def cancelarThread(self):
        if(self.hilo is not None and self.hilo.isRunning()):
            self.hilo.terminate()
            self.pbrBucles.setValue(0)
            self.btnEjecutarBucles.setEnabled(True)
        else:
            MessageBox.Show("No hay Hilos ejecutandose")
    
    def mostrarProgreso(self, n):
        self.pbrBucles.setValue(n)
    
    def mostrarRptaFinal(self, rpta):
        self.btnEjecutarBucles.setEnabled(True)
        MessageBox.Show("La suma de los {0} primeros numeros es {1}".format(self.numBucles, rpta))

class WorkerBucles(QThread):
    finalizado = QtCore.pyqtSignal(str)
    progreso = QtCore.pyqtSignal(int)
    
    def __init__(self, parent):
        super(WorkerBucles, self).__init__(parent) 
        self.numBucles = parent.numBucles
    
    def run(self):
        bloque = self.numBucles / 100
        #Aqui ejecutar el codigo que demora
        s = 0
        c = 0
        for i in range(self.numBucles):
            s = s + i
            if(i % bloque == 0):
                c=c+1
                self.progreso.emit(c)
        self.finalizado.emit(str(s))

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())