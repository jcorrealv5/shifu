import sys, os
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QDirModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo34.ui", self)
        
        cvwExplorador = self.findChild(QtWidgets.QColumnView, "cvwExplorador")
        cvwExplorador.doubleClicked.connect(self.selecionarRuta)
        btnObtenerRutaSeleccionada = self.findChild(QtWidgets.QPushButton, "btnObtenerRutaSeleccionada")
        btnObtenerRutaSeleccionada.clicked.connect(self.obtenerRutaSeleccionada)
        self.lblRutaSeleccionada = self.findChild(QtWidgets.QLabel, "lblRutaSeleccionada")
        
        self.modelo = QDirModel()
        cvwExplorador.setModel(self.modelo)
    
    def selecionarRuta(self, indice):
        self.Ruta = self.modelo.filePath(indice)
        self.lblRutaSeleccionada.setText(self.Ruta)
        if(os.path.isfile(self.Ruta)):
            os.startfile(self.Ruta)
        
    def obtenerRutaSeleccionada(self):
        self.lblRutaSeleccionada.setText(self.Ruta)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())