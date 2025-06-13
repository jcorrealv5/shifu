window.onload = function(){
	var cliente = sessionStorage.getItem("Cliente");
	var campos = cliente.split("|");
	Gui.MostrarValoresControles("C", campos);
	
	mostrarDetalles();	
	
	btnRegresar.onclick = function(){
		window.location.href = "Categorias";
	}
	
	btnGrabar.onclick = async function(){
		var detalles = [];
		var objDetalles = sessionStorage.getItem("Detalles");
		if(objDetalles!= null && objDetalles.toString()!=""){
			detalles = objDetalles.toString().split(";");
		}
		if(detalles.length>0){
			var data = txtIdCliente.value;
			data += "|12_";
			var nDetalles = detalles.length;
			var campos = [];
			for(var i=0;i<nDetalles;i++){
				campos = detalles[i].split("|");
				data += campos[0];
				data += "|";
				data += campos[2];
				data += "|";
				data += campos[3];
				if(i<nDetalles-1) data += ";";
			}
			var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
			var frm = new FormData();
			frm.append("Data", data);
			frm.append("csrfmiddlewaretoken", token);
			var rptaHttp = await fetch("GrabarOrden", 
			{
				method: "POST",
				body: frm
			});
			if(rptaHttp.ok){
				var rptaTexto = await rptaHttp.text();
				if(rptaTexto!="")
				{
					var campos = rptaTexto.split("|");
					txtIdOrden.value = campos[0];
					txtFechaOrden.value = campos[1];
					alert("Se creo la orden: " + campos[0]);
				}
				else{
					alert("Ocurrio un error al Grabar la Orden");
				}
			}
		}
		else{
			alert("No hay detalles que grabar");
		}
	}
}

function mostrarDetalles(){
	var objDetalles = sessionStorage.getItem("Detalles");
	if(objDetalles!= null){
		var detalles = objDetalles.toString().split(";");
		detalles.splice(0,0,"int|str|float|int|float");
		detalles.splice(0,0,"100|600|100|100|100");
		detalles.splice(0,0,"Codigo|Nombre del Producto|Pre Unit|Cant|Pre Total");
		Gui.Grilla(detalles, divDetalle, "|", null, null, 20, 10, ";",
		"", true, false, "", false, false, false, [2,3,4]);
	}
}

async function editarRegistro(fila, id, imgEditar){	
	imgEliminar = imgEditar.nextSibling;
	if(imgEditar.title=="Editar Registro"){
		imgEditar.src = "/static/static/Images/Carrito/Actualizar.png";
		imgEditar.title = "Grabar Cantidad"
		var cantidad = fila.childNodes[3].innerText;
		var html = "<input type='text' style='width:50px' maxlength='3' value='";
		html += cantidad;
		html += "' data-val='";
		html += cantidad;
		html += "' class='N'/>";
		fila.childNodes[3].innerHTML=html;
		imgEliminar.title="Cancelar Edicion";
		Validacion.ValidarNumerosEnlinea("N");
	}
	else{
		var txtCantidad = fila.childNodes[3].firstChild;
		if(txtCantidad.value==""){
			alert("Ingresa la cantidad");
			txtCantidad.focus();
			return;
		}
		var rptaHttp = await fetch("ObtenerStockProductoPorId?id=" + id);
		if(rptaHttp.ok){
			var data = await rptaHttp.text();
			if(data!=""){
				var stock = +data;
				var cantidad = +txtCantidad.value;
				if(cantidad>stock) {
					alert("Cantidad supera al stock de: " + stock);
					txtCantidad.value="";
					txtCantidad.focus();
					return;
				}					
				imgEditar.src = "/static/static/Images/Carrito/Editar.png";
				imgEditar.title = "Editar Registro";
				imgEliminar.title="Eliminar Registro";				
				
				var codigo = fila.childNodes[0].innerText;
				var nombre = fila.childNodes[1].innerText;
				var preUnit = +fila.childNodes[2].innerText;
				var preTotal = preUnit * cantidad;
				var detalle = codigo + "|" + nombre + "|" + preUnit + "|" + cantidad + "|" + preTotal;
				var pos = buscarProducto(codigo);
				if(pos>-1){
					var objDetalles = sessionStorage.getItem("Detalles");
					var detalles = objDetalles.toString().split(";");
					detalles[pos] = detalle;
					sessionStorage.setItem("Detalles", detalles.join(";"));
					mostrarDetalles();
				}
			}
		}			
	}
}

function eliminarRegistro(id, imgEliminar){
	var fila = imgEliminar.parentNode.parentNode;	
	if(imgEliminar.title=="Eliminar Registro"){
		var objDetalles = sessionStorage.getItem("Detalles");
		if(objDetalles!= null){
			var detalles = objDetalles.toString().split(";");
			var pos = buscarProducto(id);
			if(pos>-1){
				detalles.splice(pos,1);
				sessionStorage.setItem("Detalles", detalles.join(";"));
				mostrarDetalles();
			}
		}
	}
	else{
		var cantidadInicial = fila.childNodes[3].firstChild.getAttribute("data-val");
		fila.childNodes[3].innerHTML = cantidadInicial;
		imgEliminar.title="Eliminar Registro";
		var imgEditar = imgEliminar.previousSibling;
		imgEditar.src = "/static/static/Images/Carrito/Editar.png";
		imgEditar.title="Editar Registro";
	}
}

function seleccionarFila(idDiv, fila, idReg){
	
}

function buscarProducto(idBuscado){
	var pos = -1;
	var objDetalles = sessionStorage.getItem("Detalles");
	if(objDetalles!= null){
		var detalles = objDetalles.toString().split(";");
		var nDetalles = detalles.length;
		var campos = [];
		for(var i=0;i<nDetalles;i++){
			campos = detalles[i].split("|");
			if(campos[0]==idBuscado){
				pos = i;
				break;
			}
		}
	}
	return pos;
}