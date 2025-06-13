var id = "";
var files = [];
var nFiles = 0;
var cFiles = 0;
var sizeBloque = 100 * 1024;
var nBloques = 0;
var cBloques = 0;
var nBloquesTotal = 0;
var cBloquesTotal = 0;
var html = "";

window.onload = async function(){
	Popup.Resize(divPopupWindow, 30, 70);
	Popup.Resize(divFilesPopup, 50, 60);
	Popup.ConfigurarArrastre(divPopupContainer, divPopupWindow, divBarra);
	Validacion.ValidarNumerosEnlinea("E");
	Validacion.ValidarDecimalesEnlinea("D");
	
	var rptaHttp = await fetch("ObtenerListas");
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		var listas = rpta.split("_");
		var listaProducto = listas[0].split("¬");
		var listaProveedor = listas[1].split("¬");
		var listaCategoria = listas[2].split("¬");
		var botones = [{"id": "btnFiles", "titulo": "Files", "cabecera": "Operacion"}];
		Gui.Grilla(listaProducto, divProducto, "|", null, null, 12, 10, "¬", "", true, true, "", true, true,
        true, null, true, botones);
		Gui.Combo(listaProveedor, cboProveedor, "|", "Seleccione");
		Gui.Combo(listaCategoria, cboCategoria, "|", "Seleccione");
	}
	
	btnCerrar.onclick = btnCancelar.onclick = function(){
		divPopupContainer.style.display="none";
	}
	
	btnCerrar2.onclick = function(){
		divFilesContainer.style.display="none";
	}
	
	btnGrabar.onclick = async function(){
		if(Gui.ValidarControles("R", "L")){			
			spnValida.innerText = "";
			var data = Gui.ObtenerValoresControles("M", "|");
			var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
			var frm = new FormData();
			frm.append("Data", data);
			frm.append("csrfmiddlewaretoken", token);
			var rptaHttp = await fetch("GrabarProducto", 
			{
				method: "POST",
				body: frm
			});
			if(rptaHttp.ok){
				var rpta = await rptaHttp.text();
				if(rpta!=""){
					var listas = rpta.split("_");
					var listaProducto = listas[0].split("¬");
					id = listas[1];					
					var botones = [{"id": "btnFiles", "titulo": "Files", "cabecera": "Operacion"}];
					Gui.Grilla(listaProducto, divProducto, "|", null, null, 12, 10, "¬", "", true, true, "", true, true,
					true, null, true, botones);
					if(nFiles>0){
						cFiles = 0;
						cBloques = 0;
						cBloquesTotal = 0;
						enviarBloqueArchivo();
					}
					else {						
						alert("Se grabo el producto con id: " + id);
						divPopupContainer.style.display="none";
					}
				}
				else alert("Ocurrio un error al Grabar el Producto");
			}
		}
		else spnValida.innerText = "Datos Son Requeridos";
	}
	
	lstArchivos.ondrop = function(event){
		event.preventDefault();
		if (event.dataTransfer.items) {
			cFiles=0;
			nFiles = event.dataTransfer.items.length;
			nBloquesTotal = 0;
			[...event.dataTransfer.items].forEach((item, i) => {
			  if (item.kind === "file") {
				const file = item.getAsFile();
				leerArchivo(file);
			  }
			});			
		}		
	}
	
	lstArchivos.ondragover = function(event){
		event.preventDefault();
	}
}

function leerArchivo(file){
	cFiles++;
	html += "<option>";
	html += file.name;
	html += "</option>";
	files.push(file);
	var _Bloques = Math.floor(file.size / sizeBloque);
	if(file.size % sizeBloque >0) _Bloques++;
	nBloquesTotal += _Bloques;
	if(cFiles == nFiles){
		progreso.max = nBloquesTotal;
		lstArchivos.innerHTML = html;
		spnTotalArchivos.innerHTML = nFiles;
		cFiles = 0;
	}
}

function nuevoRegistro(){
	html = "";
	nFiles = 0;
	cFiles = 0;
	spnValida.innerText = "";
	progreso.value=0;
	nBloquesTotal = 0;
	spnTotalArchivos.innerHTML = "";
	divPopupContainer.style.display="inline";
	lstArchivos.innerHTML = "";
	Gui.LimpiarControles("M");
}

async function editarRegistro(fila, id, btn){
	nuevoRegistro();
	var rptaHttp = await fetch("ObtenerProductoPorId?id=" + id);
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();		
		var campos = rpta.split("|");
		Gui.MostrarValoresControles("M", campos);
	}
}

async function eliminarRegistro(id, btn){
	if(confirm("Seguro de eliminar al Producto: " + id)){
		var rptaHttp = await fetch("EliminarProductoPorId?id=" + id);
		if(rptaHttp.ok){
			var rpta = await rptaHttp.text();		
			if(rpta!=""){
				var listas = rpta.split("_");
				var listaProducto = listas[0].split("¬");
				var id = listas[1];
				divPopupContainer.style.display="none";
				var botones = [{"id": "btnFiles", "titulo": "Files", "cabecera": "Operacion"}];
				Gui.Grilla(listaProducto, divProducto, "|", null, null, 12, 10, "¬", "", true, true, "", true, true,
				true, null, true, botones);
				alert("Se elimino el producto con id: " + id);
			}
			else alert("Ocurrio un error al Eliminar el Producto");
		}
	}	
}

async function seleccionarBoton(idGrilla, idRegistro, idBoton, fila){
	if(idGrilla=="divProducto" && idBoton=="btnFiles"){
		var rptaHttp = await fetch("ListarArchivos?id=" + idRegistro);
		if(rptaHttp.ok){		
			var rptaTexto = await rptaHttp.text();
			if(rptaTexto!=""){
				id = idRegistro;
				divFilesContainer.style.display="inline";
				var listaArchivos = rptaTexto.split(";");
				var botones = [{"id": "btnDownload", "titulo": "Download", "cabecera": "Operacion"}];
				Gui.Grilla(listaArchivos, divFiles, "|", null, null, 6, 10, ";", "", false, false, "", false, false,
				false, null, false, botones);			
			}
			else alert("El Producto No tiene Archivos");
		}	
	}
	if(idGrilla=="divFiles" && idBoton=="btnDownload"){
		var nombreArchivo = fila.childNodes[0].innerText;
		//alert("Bajando Archivo: " + id + " - " + nombreArchivo);
		var rptaHttp = await fetch("ObtenerArchivo?id=" + id + "&nombre=" + nombreArchivo);
		if(rptaHttp.ok){		
			var blob = await rptaHttp.blob();
			var enlace = document.createElement("a");
			enlace.download = nombreArchivo;
			enlace.href = URL.createObjectURL(blob);
			enlace.click();
		}
	}
}

async function enviarBloqueArchivo(){
	var file = files[cFiles];	
	if(cBloques==0){
		nBloques = Math.floor(file.size / sizeBloque);
		if(file.size % sizeBloque >0) nBloques++;		
	}
	var inicioBloque = cBloques * sizeBloque;
	var finBloque = inicioBloque + sizeBloque;
	var blob = file.slice(inicioBloque, finBloque);
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
	var frm = new FormData();
	frm.append("Id", id);
	frm.append("Nombre", file.name);
	frm.append("Flag", cBloques==0 ? "I" : "P");
	frm.append("Blob", blob);
	frm.append("csrfmiddlewaretoken", token);
	var rptaHttp = await fetch("GrabarBloque", 
	{
		method: "POST",
		body: frm
	});
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		if(rpta=="OK"){
			cBloquesTotal++;
			cBloques++;
			spnValida.innerText = "Archivo: " + (cFiles + 1) + "/" + nFiles + " - Bloques: " + cBloquesTotal + "/" + nBloquesTotal;
			progreso.value++;
			if(cBloques<nBloques){
				enviarBloqueArchivo();
			}
			else{
				cBloques=0;
				cFiles++;
				if(cFiles<nFiles){
					enviarBloqueArchivo();	
				}
				else{
					alert("Se Grabo el Producto con todos sus archivos");
					divPopupContainer.style.display="none";
				}
			}
		}
	}
}

function cambiarPagina(indice){
}

function seleccionarFila(idDiv, fila, id){
}