import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from PyQt5.QtGui import QStandardItemModel
from modWindowsPyQt import TableView

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo33.ui", self)
        #Obtener los controles de la GUI
        tblCurso = self.findChild(QtWidgets.QTableView, "tblCurso")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        
        #Conectar a Base de Datos y traer los datos de los Cursos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspCursoListarCabCsv")
        if(data is not None):
            if(data!=""):
                #Crear la estructura de datos para los cursos: list
                listaCursos = data.split("¬")
                #Crear el Modelo
                modelo = QStandardItemModel()
                TableView.CrearTabla(listaCursos, tblCurso, modelo, [0,1])
                #Mostrar el Total de Cursos
                lblTotalRegistros.setText(str(modelo.rowCount()))
            else:
                print("No hay cursos en la tabla")
        else:
            print("Ocurrio un error al listar los cursos")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())