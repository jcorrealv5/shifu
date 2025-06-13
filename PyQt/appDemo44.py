import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QMessageBox, QHeaderView
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from modWindowsPyQt import CustomTableViewModel

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo44.ui", self)
        tblProfesor = self.findChild(QtWidgets.QTableView, "tblProfesor")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        #Acceso a Datos usando la clase clienteSQL
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        con = clienteSQL(archivoConfig, archivoLog)
        data = con.EjecutarComandoCadena("uspProfesorListarCabCsv")
        dlg = QMessageBox()
        if(data is not None):
            if(data!=""):
                listaProfesores = data.split("¬")
                formatoFilas = {"ColorTextoPar": "white", "ColorFondoPar": "red",
                                "ColorTextoImpar": "green", "ColorFondoImpar": "yellow"}
                rutaImagenesFS = {"0": "C:/Users/jhonf/Documents/Shifu/Profesores/",
                                  "4": "C:/Users/jhonf/Documents/Shifu/Huellas/"}
                modelo = CustomTableViewModel(listaProfesores, formatoFilas=formatoFilas, rutaImagenesFS=rutaImagenesFS)
                #Enlazar el Modelo a Control Vista: QTableView
                tblProfesor.setModel(modelo)
                #Configurar los anchos del control
                anchos = listaProfesores[1].split("|")
                nCampos = len(anchos)
                for j in range(nCampos):
                    tblProfesor.setColumnWidth(j, int(anchos[j]))
                #Mostrar el Numero de Registros desde el Modelo
                lblTotalRegistros.setText(str(modelo.rowCount()))
                #Ajustar los tamanios de las columnas
                tblProfesor.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            else:
                dlg.setText("No existe registros de Alumnos")
                dlg.exec()
        else:
            dlg.setText("Ocurrio un Error al Listar los Alumnos")
            dlg.exec()

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())