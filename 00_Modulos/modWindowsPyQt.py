import os, base64
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QTreeWidgetItem
from PyQt5.QtGui import QPixmap, QImage, QStandardItem

class TableWidget():
    def LlenarConLista(tbl, lista, soloLectura=True, colImagen=-1, rutaImagen=""):
        nRegistros = len(lista)
        cabeceras = lista[0].split("|")
        anchos = lista[1].split("|")
        nCabeceras = len(cabeceras)
        tbl.setRowCount(nRegistros-2)
        tbl.setColumnCount(nCabeceras)
        tbl.setHorizontalHeaderLabels(cabeceras)
        for j in range(nCabeceras):
            tbl.setColumnWidth(j, int(anchos[j]))
        for i in range(2, nRegistros):            
            campos = lista[i].split("|")
            if(colImagen>-1):
                tbl.setRowHeight(i-2, 100)
            for j in range(nCabeceras):
                if(j==colImagen):
                    item = QTableWidgetItem()
                    if(rutaImagen==""):
                        if(campos[j]!=""):
                            bytesBase64 = campos[j].encode("ascii")
                            buffer = base64.b64decode(bytesBase64)
                            qImg = QImage()
                            qImg.loadFromData(buffer)
                            pix = QPixmap(qImg)
                            item.setData(Qt.DecorationRole, pix.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))             
                        else:
                            item.setData(Qt.DecorationRole, QPixmap(None))
                    else:
                        archivo = os.path.join(rutaImagen, campos[0] + ".jpg")                        
                        if(os.path.isfile(archivo)):
                            pix = QPixmap(archivo)
                            item.setData(Qt.DecorationRole, pix.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                        else:
                            item.setData(Qt.DecorationRole, QPixmap(None))
                else:
                    item = QTableWidgetItem(campos[j])                        
                tbl.setItem(i-2, j, item)
                if(soloLectura):
                    item.setFlags(QtCore.Qt.ItemIsEnabled)                

class TreeWidget():
    def LlenarCon2Listas(tree, listaCabecera, listaDetalle, colRelDetalle=0, expandir=False):
        nCabeceras = len(listaCabecera)
        nDetalles = len(listaDetalle)
        c=0
        pos=0
        for i in range(nCabeceras):
            cabecera = listaCabecera[i].split("|")
            nodoRaiz = QTreeWidgetItem()
            nodoRaiz.setText(0, cabecera[0])
            nodoRaiz.setText(1, cabecera[1])            
            tree.addTopLevelItem(nodoRaiz)
            if(expandir):
                nodoRaiz.setExpanded(True)
            for j in range(pos, nDetalles):
                c=c+1
                detalle = listaDetalle[j].split("|")
                if(detalle[colRelDetalle]==cabecera[0]):                        
                    nodoHijo = QTreeWidgetItem()
                    nodoHijo.setText(0, detalle[0])
                    nodoHijo.setText(1, detalle[1])                    
                    nodoRaiz.addChild(nodoHijo)
                else:
                    pos = j
                    break        

class TableView():
    def CrearTabla(lista, tabla, modelo, colsSoloLectura=[]):
        cabeceras = lista[0].split("|")
        anchos = lista[1].split("|")
        nRegistros = len(lista)
        nCampos = len(cabeceras)                
        #Configurar las Cabeceras del Modelo
        modelo.setHorizontalHeaderLabels(cabeceras)                
        #Llenar el Modelo con la data de la lista
        for i in range(2, nRegistros):
            campos = lista[i].split("|")
            for j in range(nCampos):
                item = QStandardItem(campos[j])
                #Configurar Solo Lectura la primera columna: Codigo
                if(len(colsSoloLectura)>0 and j in colsSoloLectura):
                    item.setFlags(Qt.NoItemFlags)
                modelo.setItem(i-2,j,item)
        #Enlazar el Modelo a la Vista o Control View
        tabla.setModel(modelo)
        #Configurar los Anchos del Control
        for j in range(nCampos):
            tabla.setColumnWidth(j,int(anchos[j]))
    