import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo04.ui", self)
        #Obtener los controles de la UI
        self.txtNombre = self.findChild(QtWidgets.QLineEdit, "txtNombre")
        btnAceptar = self.findChild(QtWidgets.QPushButton, "btnAceptar")
        btnCancelar = self.findChild(QtWidgets.QPushButton, "btnCancelar")
        #Programar los botones de la UI
        btnAceptar.clicked.connect(self.aceptar)
        btnCancelar.clicked.connect(self.salir)

    def aceptar(self):
        msg = QMessageBox()
        msg.setText("Hola " + self.txtNombre.text())
        msg.exec()

    def salir(self):
        self.close()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())