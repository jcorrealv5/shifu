import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import TableWidget

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo23.ui", self)
        tblCurso = self.findChild(QtWidgets.QTableWidget, "tblCurso")
        #Traer los datos de los alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspCursoListarCabCsv")
        if(data is not None):
            listaCursos = data.split("¬")
            TableWidget.LlenarConLista(tblCurso, listaCursos)
        else:
            print("Ocurrio un Error al traer los cursos")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())