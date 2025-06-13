import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo19.ui", self)
        self.cboProfesor = self.findChild(QtWidgets.QComboBox, "cboProfesor")
        btnMensaje = self.findChild(QtWidgets.QPushButton, "btnMensaje")
        btnMensaje.clicked.connect(self.mostrarMensaje)
        
        #Conectar a Base de Datos y traer los Nombres de los Alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspProfesorListarNombresCsv")
        msg = QMessageBox()
        if(data is not None):
            if(data!=""):
                listaProfesores = data.split("¬")
                self.cboProfesor.addItems(listaProfesores)
            else:
                msg.setText("No hay registro de Profesores")
                msg.exec()
        else:
            msg.setText("Ocurrio un Error al Listar los Profesores")
            msg.exec()

    def mostrarMensaje(self):
        msg = QMessageBox()
        msg.setText("Seleccionastes al Profesor: " + self.cboProfesor.currentText())
        msg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())