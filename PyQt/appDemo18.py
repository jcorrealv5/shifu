import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo18.ui", self)
        lstCurso = self.findChild(QtWidgets.QListWidget, "lstCurso")
        #Conectar a Base de Datos y traer los Nombres de los Alumnos
        archivoConfig=r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspCursoListarNombresCsv")
        dlg = QMessageBox()
        if(data is not None):
            if(data!=""):
                listaCursos = data.split("¬")
                lstCurso.addItems(listaCursos)
            else:
                dlg.setText("No hay Cursos registros")
                dlg.exec()
        else:
            dlg.setText("Ocurrio un error al listar los Cursos")
            dlg.exec()            

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())