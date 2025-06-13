import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import CustomTableViewModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo38.ui", self)
        #Obtener los controles de la GUI
        tblAlumno = self.findChild(QtWidgets.QTableView, "tblAlumno")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        chkVerCabeceraFilas = self.findChild(QtWidgets.QCheckBox, "chkVerCabeceraFilas")
        chkVerCabeceraFilas.stateChanged.connect(self.ocultarCabecerasFilas)
        
        #Conectar a Base de Datos y traer los datos de los Alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspAlumnoListarCabCsv")
        if(data is not None):
            if(data!=""):
                #Crear la estructura de datos para los alumnos: list
                listaAlumnos = data.split("¬")
                self.modelo = CustomTableViewModel(listaAlumnos)
                tblAlumno.setModel(self.modelo)
                lblTotalRegistros.setText(str(self.modelo.rowCount()))
                #Configurar los Anchos del Control
                nCampos = self.modelo.columnCount()
                anchos = listaAlumnos[1].split("|")
                for j in range(nCampos):
                    tblAlumno.setColumnWidth(j,int(anchos[j]))
            else:
                print("No hay alumnos en la tabla")
        else:
            print("Ocurrio un error al listar alumnos")
    
    def ocultarCabecerasFilas(self, value):
        self.modelo.setRowHeader(value==0)

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())