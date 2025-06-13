import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QMessageBox

app = QtWidgets.QApplication([""])
dlg = QDialog()
dlg.setWindowTitle("Demo 01: Crear un Dialogo con Controles solo x codigo")

layout = QtWidgets.QVBoxLayout(dlg)
#Agregar label
lblNombre = QLabel()
lblNombre.setText("Ingresa tu Nombre:")
layout.addWidget(lblNombre)
#Agregar un texto
txtNombre = QLineEdit()
layout.addWidget(txtNombre)
#Agregar un Boton Aceptar
btnAceptar = QPushButton()
btnAceptar.setText("Aceptar")
layout.addWidget(btnAceptar)
#Agregar un Boton CAncelar
btnCancelar = QPushButton()
btnCancelar.setText("Cancelar")
layout.addWidget(btnCancelar)
#Programar el Boton Aceptar
def aceptar():
    msg = QMessageBox()
    msg.setText("Hola " + txtNombre.text())
    msg.exec()
btnAceptar.clicked.connect(aceptar)
#Programar el Boton Cancelar
def cancelar():
    dlg.close()
btnCancelar.clicked.connect(cancelar)

dlg.setFixedSize(500,150)
dlg.show()
sys.exit(app.exec_())