import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo30.ui", self)
        lvwAlumno = self.findChild(QtWidgets.QListView, "lvwAlumno")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        #Conectar a Base de Datos y traer los Nombres de los Alumnos
        archivoConfig=r"C:\Data\Python\2025_01_PythonMJ\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Data\Python\2025_01_PythonMJ\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspAlumnoListarNombresCsv")
        if(data is not None):
            if(data!=""):
                #Crear el Origen de Datos: Lista
                listaAlumnos = data.split("¬")
                #Crear un Modelo con el Origen de Datos: QStringListModel
                modelo = QStringListModel(listaAlumnos)
                #Enlazar el Modelo al Control View: QListView
                lvwAlumno.setModel(modelo)
                #Obtener el Total de Registros
                nRegistros = modelo.rowCount()
                lblTotalRegistros.setText(str(nRegistros))
            else:
                print("No existen registros en Alumnos")
        else:
            print("Ocurrio un Error al obtener los Alumnos")
        

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())