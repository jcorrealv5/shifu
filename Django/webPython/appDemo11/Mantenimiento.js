window.onload = async function(){
	Popup.Resize(divPopupWindow, 30, 40);
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
		Gui.Grilla(listaProducto, divProducto, "|", null, null, 20, 10, "¬", "", true);
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
			var frm = new URLSearchParams();
			frm.append("Data", data);
			frm.append("csrfmiddlewaretoken", token);
			var rptaHttp = await fetch("GrabarProducto", 
			{
				method: "POST",
				headers: {"Content-Type": "application/x-www-form-urlencoded",},
				body: frm
			});
			if(rptaHttp.ok){
				var rpta = await rptaHttp.text();
				if(rpta!=""){
					var listas = rpta.split("_");
					var listaProducto = listas[0].split("¬");
					var id = listas[1];
					divPopupContainer.style.display="none";
					Gui.Grilla(listaProducto, divProducto, "|", null, null, 20, 10, "¬", "", true);
					alert("Se grabo el producto con id: " + id);
				}
				else alert("Ocurrio un error al Grabar el Producto");
			}
		}
		else spnValida.innerText = "Datos Son Requeridos";
	}
}

function nuevoRegistro(){
	divPopupContainer.style.display="inline";
	Gui.LimpiarControles("M");
}

async function editarRegistro(fila, id, btn){
	divPopupContainer.style.display="inline";
	Gui.LimpiarControles("M");
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
				Gui.Grilla(listaProducto, divProducto, "|", null, null, 20, 10, "¬", "", true);
				alert("Se elimino el producto con id: " + id);
			}
			else alert("Ocurrio un error al Eliminar el Producto");
		}
	}	
}

function cambiarPagina(indice){
}

function seleccionarFila(idDiv, fila, id){
}