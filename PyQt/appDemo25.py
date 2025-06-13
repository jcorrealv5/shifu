import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import TableWidget

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo25.ui", self)
        tblProfesor = self.findChild(QtWidgets.QTableWidget, "tblProfesor")
        #Traer los datos de los Profesores
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspProfesorListarCabCsv")
        if(data is not None):
            listaProfesores = data.split("¬")
            rutaImagen = "C:/Users/jhonf/Documents/Shifu/Profesores/"
            TableWidget.LlenarConLista(tblProfesor, listaProfesores, colImagen=1, rutaImagen=rutaImagen)
        else:
            print("Ocurrio un Error al traer los Profesores")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())