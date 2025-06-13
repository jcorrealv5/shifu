import os, base64, random
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QAbstractTableModel, QSize, QSortFilterProxyModel
from PyQt5.QtWidgets import QTableWidgetItem, QTreeWidgetItem, QMessageBox, QHeaderView, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QImage, QStandardItem, QColor, QPainter, QImage, QFont

class MessageBox():
    def Show(texto):
        dlg = QMessageBox()
        dlg.setText(texto)
        dlg.exec()

class ComboBox():
    def LlenarDosCols(cbo, lista, sepCampo="|", primerItem=""):
        if(primerItem!=""):
            cbo.addItem(primerItem, "")
        nRegistros = len(lista)
        for i in range(nRegistros):
            campos = lista[i].split(sepCampo)
            cbo.addItem(campos[1], campos[0])        

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
    
    def ConfigurarAnchos(tabla, anchos):
        nCampos = len(anchos)
        for j in range(nCampos):
            tabla.setColumnWidth(j,int(anchos[j]))

class CustomTableViewModel(QAbstractTableModel):
    def __init__(self, lista, ocultarNumFilas = False, colsSubtotales = [], textoSubtotales={}, formatoFilas = {}, rutaImagenesFS = {}, columnaCheck=False, esFloat=False, 
                 soloLectura=True, numColsExtras=0):
        QAbstractTableModel.__init__(self)
        self.cabeceras = lista[0].split("|")
        self.tipos = lista[2].split("|")        
        self.lista = lista[3:]
        self.nRegistros = len(self.lista)
        self.nCampos = len(self.cabeceras)
        self.ocultarNumFilas = ocultarNumFilas
        self.colsSubtotales = colsSubtotales
        self.textoSubtotales = textoSubtotales
        self.formatoFilas = formatoFilas
        self.rutaImagenesFS = rutaImagenesFS
        self.columnaCheck = columnaCheck
        self.esFloat = esFloat
        self.soloLectura = soloLectura
        self.numColsExtras = numColsExtras
        
        if(self.columnaCheck):
            self.checks = []
            for i in range(self.nRegistros):
                self.checks.append(0)
        
        if(len(self.colsSubtotales)>0):
            self.valsSubtotales = []
            for j in range(len(colsSubtotales)):
                self.valsSubtotales.append(0)
            for i in range(self.nRegistros):
                campos = self.lista[i].split("|")
                for j in range(self.nCampos):
                    if(j in self.colsSubtotales):
                        pos = self.colsSubtotales.index(j)
                        tipo = self.tipos[j]
                        if(tipo=="int"):
                            self.valsSubtotales[pos] += int(campos[j])
                        if(tipo=="float"):
                            self.valsSubtotales[pos] += float(campos[j])            
    
    def rowCount(self, parent=None):
        if(len(self.colsSubtotales)>0):
            return self.nRegistros + 1
        else:
            return self.nRegistros
    
    def columnCount(self, parent=None):
        return self.nCampos + self.numColsExtras
    
    def headerData(self, seccion, orientacion, rol):
        if(orientacion==Qt.Horizontal and rol==Qt.DisplayRole):
            if(seccion<self.nCampos):
                return self.cabeceras[seccion]
        if(not self.ocultarNumFilas):
            if(orientacion==Qt.Vertical and rol==Qt.DisplayRole):
                return seccion+1
    
    def flags(self, index):
        if(self.soloLectura):
            return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsUserCheckable
        else:
            if(index.column()==0):
                return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsUserCheckable
            else:
                return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEditable
    
    def setData(self, index, value, role):
        if role == Qt.CheckStateRole:
            self.checks[index.row()] = value
            return True
        if role == Qt.EditRole:
            campos = self.lista[index.row()].split("|")
            campos[index.column()] = value
            self.lista[index.row()] = "|".join(campos)
            return True
    
    def data(self, celda, rol=Qt.DisplayRole):
        fila = celda.row()
        col = celda.column()
        if(col<self.nCampos):
            tipo = self.tipos[col]
            valor=""
            if(len(self.colsSubtotales)==0 or (len(self.colsSubtotales)>0 and fila<self.nRegistros)):
                registro = self.lista[fila].split("|")
                valor = registro[col]
            if(rol==Qt.DisplayRole):
                if(len(self.colsSubtotales)==0 or (len(self.colsSubtotales)>0 and fila<self.nRegistros)):
                    if(tipo=="float"):
                        if(self.esFloat):
                            return float(valor)
                        else:
                            return "{:.{}f}".format(float(valor), 2)
                    else:
                        if(tipo=="int"):
                            return int(valor)
                        else:
                            if(tipo!="base64"):                            
                                return valor
                if(len(self.colsSubtotales)>0 and fila==self.nRegistros):                
                    if(col in self.colsSubtotales):
                        pos = self.colsSubtotales.index(col)
                        return self.valsSubtotales[pos]
                    if(str(col) in self.textoSubtotales):
                        return self.textoSubtotales[str(col)]
            if(rol==Qt.TextAlignmentRole):
                if(tipo=="int" or tipo=="float"):
                     return Qt.AlignVCenter + Qt.AlignRight
                else:
                    if(len(self.colsSubtotales)>0 and fila==self.nRegistros and str(col) in self.textoSubtotales):
                        return Qt.AlignVCenter + Qt.AlignRight
                    else:
                        return Qt.AlignVCenter + Qt.AlignLeft
            if(rol==Qt.BackgroundRole):
                if(len(self.colsSubtotales)>0 and fila==self.nRegistros):
                    return QColor("red")
                if("ColorFondoImpar" in self.formatoFilas and fila % 2==0):
                    return QColor(self.formatoFilas["ColorFondoImpar"])
                if("ColorFondoPar" in self.formatoFilas and fila % 2!=0):
                    return QColor(self.formatoFilas["ColorFondoPar"])
            if(rol==Qt.ForegroundRole):
                if(len(self.colsSubtotales)>0 and fila==self.nRegistros):
                    return QColor("white")
                if("ColorTextoImpar" in self.formatoFilas and fila % 2==0):
                    return QColor(self.formatoFilas["ColorTextoImpar"])
                if("ColorTextoPar" in self.formatoFilas and fila % 2!=0):
                    return QColor(self.formatoFilas["ColorTextoPar"])
            if(rol==Qt.DecorationRole):
                if(tipo=="base64"):
                    base64Bytes = valor.encode("ascii")
                    buffer = base64.b64decode(base64Bytes)
                    pix = QPixmap()
                    pix.loadFromData(buffer)
                    bmp = pix.scaled(80, 80, Qt.KeepAspectRatio)
                    return bmp
                if(tipo=="fs" and str(col) in self.rutaImagenesFS):
                    archivoImagen = os.path.join(self.rutaImagenesFS[str(col)], valor + ".jpg")                
                    if(os.path.isfile(archivoImagen)):
                        pix = QPixmap(archivoImagen)
                        bmp = pix.scaled(80, 80, Qt.KeepAspectRatio)
                        return bmp
            if(rol==Qt.SizeHintRole):
                if(tipo=="base64"):
                    return QSize(100,80)
                if(tipo=="fs"):
                    return QSize(100,120)
            if(rol==Qt.CheckStateRole):
                if(self.columnaCheck and col==0):
                    return self.checks[fila]
            
    def setRowHeader(self, ocultarNumFilas):
        self.ocultarNumFilas = ocultarNumFilas
        self.headerDataChanged.emit(Qt.Vertical, 0, self.nRegistros - 1)
        return self.ocultarNumFilas

    def setChecks(self, valor):
        if(self.columnaCheck):
            for i in range(self.nRegistros):
                indice = self.index(i,0)
                self.setData(indice, valor, Qt.CheckStateRole) 
            self.layoutChanged.emit()
    
    def getChecks(self, col):
        valores = []
        if(self.columnaCheck):
            for i in range(self.nRegistros):
                if self.checks[i]==2:
                    registro = self.lista[i].split("|")
                    valor = registro[col]
                    valores.append(valor)
        return valores
    
    def insertRow(self, position, index=QtCore.QModelIndex()):
        self.insertRows(position, 1, index)

    def insertRows(self, position, rows=1, index=QtCore.QModelIndex()):
        self.beginInsertRows(index, position, position + rows - 1)
        for row in range(0, rows):
            self.lista.append("0||1|1|0|0")
        self.endInsertRows()        
        return True
    
    def removeRow(self, position, index=QtCore.QModelIndex()):
        print("Eliminando: ", position)
        self.beginRemoveRows(index, position, position)
        print("nRegistros Antes: ", self.nRegistros)
        del self.lista[position]
        self.nRegistros=self.nRegistros-1
        print("nRegistros Despues: ", self.nRegistros)
        self.endRemoveRows()
        self.layoutChanged.emit()

class SortFilterProxyModel(QSortFilterProxyModel):   
    def __init__(self, parent=None):
        super(SortFilterProxyModel, self).__init__(parent)
        self.valor = ""
        self.c = 0
    
    def setValueOperator(self, tipo, operador, valor):
        self.tipo = tipo
        self.operador = operador
        self.c = 0
        self.valor = valor
        self.invalidateFilter()
    
    def filterAcceptsRow(self, source_row, source_parent):
        self.c += 1
        if(self.c>self.sourceModel().rowCount()):
            return False
        if(self.valor==""):
            return True
        col = self.filterKeyColumn()
        index = self.sourceModel().index(source_row, col, source_parent)
        data = self.sourceModel().data(index, Qt.DisplayRole)
        if(data is None):
            return False
        if(self.tipo=="N"):
            if(self.operador==0):
                return (data==self.valor)
            elif(self.operador==1):
                return (data>self.valor)
            elif(self.operador==2):
                return (data<self.valor)
            elif(self.operador==3):
                return (data>=self.valor)
            elif(self.operador==4):
                return (data<=self.valor)
            elif(self.operador==5):
                return (data!=self.valor)
            else:
                return False
        else:
            if(self.tipo=="S"):
                if(self.operador==0):
                    return (data.lower().startswith(self.valor.lower()))
                elif(self.operador==1):
                    return (data.lower().endswith(self.valor.lower()))
                elif(self.operador==2):
                    return (self.valor.lower() in data.lower())
                else:
                    return False
        return False

class EditableHeaderView(QHeaderView):
    textChanged = QtCore.pyqtSignal(int, str)

    def __init__(self, parent=None, combosIndices=[], combosListas=[]):
        super(EditableHeaderView, self).__init__(QtCore.Qt.Horizontal, parent)
        self.setSectionsClickable(True)
        self.sectionDoubleClicked.connect(self.on_sectionDoubleClicked)
        self._lineedit = QLineEdit(self, visible=False)
        self._lineedit.textChanged.connect(self.on_text_changed)
        if len(combosIndices)>0:
            self._combobox = QComboBox(self, visible=False)
            self._combobox.currentIndexChanged.connect(self.on_combo_changed)
        self.col = 0
        self.combosIndices = combosIndices
        self.combosListas = combosListas
    
    @QtCore.pyqtSlot(int)
    def on_sectionDoubleClicked(self, index):
        self.col = index
        self._lineedit.hide()
        if(len(self.combosIndices)>0):
              self._combobox.hide()
        geom = QtCore.QRect(self.sectionViewportPosition(index), 0, self.sectionSize(index), self.height())
        if(len(self.combosIndices)>0 and self.col in self.combosIndices):
            pos = self.combosIndices.index(self.col)
            lista = self.combosListas[pos]
            self._combobox.clear()
            self._combobox.addItem("")
            self._combobox.addItems(lista)
            self._combobox.setGeometry(geom)
            self._combobox.show()
        else:
            self._lineedit.setText("")
            self._lineedit.setGeometry(geom)
            self._lineedit.show()
            self._lineedit.setFocus()
    
    @QtCore.pyqtSlot(str)
    def on_text_changed(self, text):
        self.textChanged.emit(self.col, text)
        
    @QtCore.pyqtSlot(int)
    def on_combo_changed(self, indice):
        text = self._combobox.currentText()
        self.textChanged.emit(self.col, text)

class Captcha():
    def Crear(ancho, alto, texto, size, nLineas, lblGrafico):
        img = QImage(ancho, alto, QImage.Format_RGB32)
        pix = QPixmap.fromImage(img)
        qp = QPainter()        
        qp.begin(pix)
        qp.fillRect(0, 0, ancho, alto, QColor("aqua"))
        qp.setFont(QFont("Arial", size))         
        n = len(texto)
        x = 20
        colores = ["white", "yellow", "red", "green", "blue", "brown"]
        for i in range(n):
            c = random.randint(0, len(colores)-1)
            y = random.randint(size, alto-size)
            qp.setPen(QColor(colores[c]))
            qp.drawText(x, y, texto[i])
            x += 40
        for j in range(nLineas):
            c = random.randint(0, len(colores)-1)
            qp.setPen(QColor(colores[c]))
            x1 = random.randint(0, ancho)
            y1 = random.randint(0, alto)
            x2 = random.randint(0, ancho)
            y2 = random.randint(0, alto)
            qp.drawLine(x1, y1, x2, y2)
        qp.end()
        lblGrafico.setPixmap(pix)
        lblGrafico.resize(ancho, alto)
