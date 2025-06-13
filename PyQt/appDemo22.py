import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QDialog, QTableWidgetItem
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo22.ui", self)
        tblAlumno = self.findChild(QtWidgets.QTableWidget, "tblAlumno")
        #Traer los datos de los alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspAlumnoListarCabCsv")
        if(data is not None):
            listaAlumnos = data.split("¬")
            nRegistros = len(listaAlumnos)
            cabeceras = listaAlumnos[0].split("|")
            anchos = listaAlumnos[1].split("|")
            nCabeceras = len(cabeceras)
            tblAlumno.setRowCount(nRegistros-2)
            tblAlumno.setColumnCount(nCabeceras)
            tblAlumno.setHorizontalHeaderLabels(cabeceras)
            for j in range(nCabeceras):
                tblAlumno.setColumnWidth(j, int(anchos[j]))
            for i in range(2, nRegistros):
                campos = listaAlumnos[i].split("|")
                for j in range(nCabeceras):
                    item = QTableWidgetItem(campos[j])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    tblAlumno.setItem(i-2, j, item)
            #tblAlumno.setEnabled(False)
        else:
            print("Ocurrio un Error al traer los alumnos")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())