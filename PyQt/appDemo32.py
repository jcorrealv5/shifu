import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog
sys.path.append("../00_Modulos")
from modAccesoDatos import clienteSQL
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Dialogo(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("dlgDemo32.ui", self)
        #Obtener los controles de la GUI
        tblAlumno = self.findChild(QtWidgets.QTableView, "tblAlumno")
        lblTotalRegistros = self.findChild(QtWidgets.QLabel, "lblTotalRegistros")
        
        #Conectar a Base de Datos y traer los datos de los Alumnos
        archivoConfig=r"C:\Users\jhonf\Documents\Shifu\Demos\00_Modulos\Config_BD_DACP_2025.txt"
        archivoLog=r"C:\Users\jhonf\Documents\Shifu\Demos\Logs\LogPyQtDemo05.txt"
        conexion = clienteSQL(archivoConfig,archivoLog)
        data = conexion.EjecutarComandoCadena("uspAlumnoListarCabCsv")
        if(data is not None):
            if(data!=""):
                #Crear la estructura de datos para los alumnos: list
                listaAlumnos = data.split("¬")
                cabeceras = listaAlumnos[0].split("|")
                anchos = listaAlumnos[1].split("|")
                nRegistros = len(listaAlumnos)
                nCampos = len(cabeceras)                
                #Crear el Modelo
                modelo = QStandardItemModel()
                #Configurar las Cabeceras del Modelo
                modelo.setHorizontalHeaderLabels(cabeceras)                
                #Llenar el Modelo con la data de la lista
                for i in range(2, nRegistros):
                    campos = listaAlumnos[i].split("|")
                    for j in range(nCampos):
                        item = QStandardItem(campos[j])
                        #Configurar Solo Lectura la primera columna: Codigo
                        if(j==0):
                            item.setFlags(Qt.NoItemFlags)
                        modelo.setItem(i-2,j,item)
                #Enlazar el Modelo a la Vista o Control View
                tblAlumno.setModel(modelo)
                #Configurar los Anchos del Control
                for j in range(nCampos):
                    tblAlumno.setColumnWidth(j,int(anchos[j]))
                #Mostrar el Total de Alumnos
                lblTotalRegistros.setText(str(modelo.rowCount()))
            else:
                print("No hay alumnos en la tabla")
        else:
            print("Ocurrio un error al listar alumnos")

app = QtWidgets.QApplication(sys.argv)
dlg = Dialogo()
dlg.show()
sys.exit(app.exec_())