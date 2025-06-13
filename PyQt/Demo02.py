import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox

app = QtWidgets.QApplication([""])
dlg = QDialog()
uic.loadUi("dlgDemo02.ui", dlg)

txtNombre = dlg.findChildren(QtWidgets.QLineEdit, "txtNombre")
btnAceptar = dlg.findChildren(QtWidgets.QPushButton, "btnAceptar")
btnCancelar = dlg.findChildren(QtWidgets.QPushButton, "btnCancelar")


def aceptar():
    msg = QMessageBox()
    msg.setText("Hola " + txtNombre.text())
    msg.exec()
btnAceptar.clicked.connect(aceptar)
def salir():
    dlg.close()
btnCancelar.clicked.connect(salir)

dlg.show()
sys.exit(app.exec_())