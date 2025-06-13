import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo05p.ui", self)
        #Obtener los controles a programar
        txtCodigo = self.findChild(QtWidgets.Qpi, "txtCodigo")
        btnConsultar = self.findChild(QtWidgets.QPushButton, "btnConsultar")
        txtApellidos = self.findChild(QtWidgets.QLineEdit, "txtApellidos")
        txtNombres = self.findChild(QtWidgets.QLineEdit, "txtNombres")
        txtCorreo = self.findChild(QtWidgets.QLineEdit, "txtCorreo")
        self.contador = 0
        #Programar los eventos de los controles
        btnConsultar.clicked.connect(self.consultarRegistro)
    
    def consultarRegistro(self):
        self.contador += 1
        print("Nro de Clicks: " + str(self.contador))


app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())