var file = null;

window.onload = async function(){
	Popup.Resize(divPopupWindow, 30, 60);
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
		var botones = [{"id": "btnPreview", "titulo": "Preview", "cabecera": "Operacion"}];
		Gui.Grilla(listaProducto, divProducto, "|", null, null, 12, 10, "¬", "", true, true, "", true, true,
        true, null, true, botones);
		Gui.Combo(listaProveedor, cboProveedor, "|", "Seleccione");
		Gui.Combo(listaCategoria, cboCategoria, "|", "Seleccione");
	}
	
	btnCerrar.onclick = btnCancelar.onclick = function(){
		divPopupContainer.style.display="none";
	}
	
	btnGrabar.onclick = async function(){
		if(Gui.ValidarControles("R", "L")){			
			spnValida.innerText = "";
			var data = Gui.ObtenerValoresControles("M", "|");
			var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
			var frm = new FormData();
			frm.append("Data", data);
			frm.append("csrfmiddlewaretoken", token);
			if(file!=null){
				frm.append("Archivo", file);
			}
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
					var id = listas[1];
					divPopupContainer.style.display="none";
					var botones = [{"id": "btnPreview", "titulo": "Preview", "cabecera": "Operacion"}];
					Gui.Grilla(listaProducto, divProducto, "|", null, null, 12, 10, "¬", "", true, true, "", true, true,
					true, null, true, botones);
					alert("Se grabo el producto con id: " + id);
				}
				else alert("Ocurrio un error al Grabar el Producto");
			}
		}
		else spnValida.innerText = "Datos Son Requeridos";
	}
	
	imgFileSystem.onclick = function(){
		divPreviewContainer.style.display="none";
	}
	
	btnArchivo.onclick = function(){
		fupImagen.click();
	}
	
	fupImagen.onchange = function(){
		file = this.files[0];
		txtArchivo.value = file.name;
		var reader = new FileReader();
		if (reader != null) {
			reader.onloadend = function () {
				imgPreview.src = reader.result;
			};
			reader.readAsDataURL(file);
		}
	}
}

function nuevoRegistro(){
	divPopupContainer.style.display="inline";
	file = null;
	txtArchivo.value="";
	imgPreview.src = "";	
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
				var botones = [{"id": "btnPreview", "titulo": "Preview", "cabecera": "Operacion"}];
				Gui.Grilla(listaProducto, divProducto, "|", null, null, 12, 10, "¬", "", true, true, "", true, true,
				true, null, true, botones);
				alert("Se elimino el producto con id: " + id);
			}
			else alert("Ocurrio un error al Eliminar el Producto");
		}
	}	
}

async function seleccionarBoton(idGrilla, idRegistro, idBoton, fila){
	var rptaHttp = await fetch("ObtenerImagen?id=" + idRegistro);
	if(rptaHttp.ok){
		divPreviewContainer.style.display="inline";
		var blob = await rptaHttp.blob();
		var nTotal = blob.size;
		if(nTotal>0){
			var blobImagen = new Blob([blob], { "type": "image/jpeg" });
			imgFileSystem.src = URL.createObjectURL(blobImagen);
		}
	}
}

function cambiarPagina(indice){
}

function seleccionarFila(idDiv, fila, id){
}