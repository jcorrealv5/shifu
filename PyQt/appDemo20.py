import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo20.ui", self)
        self.cboAlumno = self.findChild(QtWidgets.QComboBox, "cboAlumno")
        self.cboCurso = self.findChild(QtWidgets.QComboBox, "cboCurso")
        self.cboProfesor = self.findChild(QtWidgets.QComboBox, "cboProfesor")
        self.Listas = []
        self.Listas.append(self.cboAlumno)
        self.Listas.append(self.cboCurso)
        self.Listas.append(self.cboProfesor)
        btnMensaje = self.findChild(QtWidgets.QPushButton, "btnMensaje")
        btnMensaje.clicked.connect(self.mostrarMensaje)
        
        #Conectar a Base de Datos y traer los Nombres de los Alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspAlumnoCursoProfesorListasCsv")
        msg = QMessageBox()
        if(data is not None):
            if(data!=""):
                listas = data.split("_")
                nListas = len(listas)
                self.nombreTablas = listas[0].split("|")
                for i in range(1, nListas):
                    if(listas[i]!=""):
                        lista = listas[i].split("¬")
                        self.Listas[i-1].addItems(lista)
                    else:
                        print("No existe registros de " + self.nombreTablas[i-1])
        else:
            msg.setText("Ocurrio un Error al obtener las Listas de Alumnos, Cursos y Profesores")
            msg.exec()

    def mostrarMensaje(self):
        rpta = ""
        nTablas = len(self.nombreTablas)
        for i in range(nTablas):
            rpta += self.nombreTablas[i]
            rpta += " = "
            rpta += self.Listas[i].currentText()
            rpta += "\r\n"
        msg = QMessageBox()
        msg.setText(rpta)
        msg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())