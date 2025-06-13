class Pdf():
    def ExportarDesdeLista(lista, cabeceras, anchos, titulo, archivo, regPag = 20):
        nfilas = len(lista)
        ncampos = len(lista[0])
        print("ncampos: ", ncampos)
        nhojas = nfilas // regPag
        if (nfilas % 20 > 0):
            nhojas = nhojas + 1
        ancho = 0
        anchoTotal = 0
        cr = 0
        sw = open(archivo, "w")
        sw.write("%PDF-1.4\n")
        sw.write("1 0 obj <</Type /Catalog /Pages 2 0 R>>\n")
        sw.write("endobj\n")
        sw.write("2 0 obj <</Type /Pages /Kids [\n")
        for k in range(nhojas):
            sw.write(str((k * 4) + 3))
            sw.write(" 0 R ")
        sw.write("] /Count ")
        sw.write(str(nhojas))
        sw.write(">>\n")
        sw.write("endobj\n")
        for k in range(nhojas):
            sw.write(str((k * 4) + 3))
            sw.write(" 0 obj <</Type /Page /Parent 2 0 R /Resources 4 0 R /MediaBox [0 0 600 800]/Contents ")
            sw.write(str((k * 4) + 6))
            sw.write(" 0 R>>\n")
            sw.write("endobj\n")
            sw.write(str((k * 4) + 4))
            sw.write(" 0 obj <</Font <</F1 5 0 R>>>>\n")
            sw.write("endobj\n")
            sw.write(str((k * 4) + 5))
            sw.write(" 0 obj <</Type /Font /Subtype /Type1 /BaseFont /Helvetica>>\n")
            sw.write("endobj\n")
            sw.write(str((k * 4) + 6))
            sw.write(" 0 obj\n")
            sw.write("<</Length 44>>\n")
            sw.write("stream\n")
            sw.write("BT")
            sw.write("/F1 16 Tf 50 750 Td 0 Tr 0.5 g (")
            sw.write(titulo)
            sw.write(")Tj ")
            sw.write("/F1 10 Tf 0 g ")
            sw.write("0 -30 Td (")
            sw.write(cabeceras[0])
            sw.write(")Tj ")
            anchoTotal = 0
            for j in range(1, ncampos):
                ancho = anchos[j - 1] // 2
                sw.write(str(ancho))
                sw.write(" 0 Td (")
                sw.write(cabeceras[j])
                sw.write(")Tj ")
                anchoTotal = anchoTotal + ancho
            for i in range(regPag):
                if (cr < nfilas):
                    sw.write("-")
                    sw.write(str(anchoTotal))
                    sw.write(" -30 Td (")
                    sw.write(str(lista[cr][0]))
                    sw.write(")Tj ")
                    for j in range(1, ncampos):
                        ancho = anchos[j - 1] // 2
                        sw.write(str(ancho))
                        sw.write(" 0 Td (")
                        sw.write(str(lista[cr][j]))
                        sw.write(")Tj ")
                    cr = cr + 1
                else:
                    break
            sw.write("ET\n")
            sw.write("endstream\n")
            sw.write("endobj\n")
        sw.write("xref\n")
        sw.write("0 7\n")
        sw.write("0000000000 65535 f\n")
        sw.write("0000000009 00000 n\n")
        sw.write("0000000056 00000 n\n")
        sw.write("0000000111 00000 n\n")
        sw.write("0000000212 00000 n\n")
        sw.write("0000000250 00000 n\n")
        sw.write("0000000317 00000 n\n")
        sw.write("trailer <</Size 7/Root 1 0 R>>\n")
        sw.write("startxref\n")
        sw.write("406\n")
        sw.write("%%EOF\n")
        sw.close()