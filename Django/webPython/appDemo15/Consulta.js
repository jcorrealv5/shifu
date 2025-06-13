var listaOrdenes = [];
var listaDetalles = [];
var c=0;
var pos=3;

window.onload = function(){
	Validacion.ValidarNumerosEnlinea("N");
	
	btnConsultar.onclick = async function(){
		if(Validacion.ValidarDatos("R","N",spnValida)){
			var idOrdenInicio = txtIdOrdenInicio.value;
			var idOrdenFin = txtIdOrdenFin.value;
			var url = "ConsultarOrdenesPorRango?inicio=" + idOrdenInicio;
			url += "&fin=" + idOrdenFin
			var rptaHttp = await fetch(url);
			if(rptaHttp.ok){
				var rpta = await rptaHttp.text();
				var listas = rpta.split("_");
				listaOrdenes = listas[0].split(";");
				listaDetalles = listas[1].split(";");
				mostrarOrdenesDetalles();
			}
		}	
	}
}

function mostrarOrdenesDetalles(){
	divReporte.innerHTML = "";
	var inicio = new Date();
	var html = "";
	var nListaOrdenes = listaOrdenes.length;
	var nListaDetalles = listaDetalles.length;
	var cabecerasOrdenes = listaOrdenes[0].split("|");
	var anchosOrdenes = listaOrdenes[1].split("|");
	var nCamposOrdenes = cabecerasOrdenes.length;
	var camposOrdenes = [];
	c = 0;
	pos=3;
	for(var i=3;i<nListaOrdenes;i++){
		camposOrdenes = listaOrdenes[i].split("|");
		html += "<table>";
		html += "<thead>";
		html += "<tr class='FilaCabecera'>";
		for(var j=0;j<nCamposOrdenes;j++){			
			html += "<th style='width:";
			html += anchosOrdenes[j];
			html += "'>";
			html += cabecerasOrdenes[j];
			html += "</th>";
		}
		html += "</tr>";
		html += "</thead>";
		html += "<tbody>";
		html += "<tr class='FilaDatos'>";
		for(var j=0;j<nCamposOrdenes;j++){
			html += "<td>";
			html += camposOrdenes[j];
			html += "</td>";
		}
		html += "</tr>";
		html += "</tbody>";
		html += "</table>";
		html += "</p>";
		html += crearTablaDetalles(camposOrdenes[0]);
	}
	divReporte.innerHTML = html;
	var fin = new Date();
	var tiempo = fin - inicio;
	spnValida.innerText = "Ordenes: " + (nListaOrdenes-3) + " - Detalles: " + (nListaDetalles-3) + " - Bucles: " + c + " - Tiempo: " + tiempo + " msg";
}

function crearTablaDetalles(idOrden) {
	var html = "";
	var nListaDetalles = listaDetalles.length;
	var cabecerasDetalles = listaDetalles[0].split("|");
	var anchosDetalles = listaDetalles[1].split("|");
	var nCamposDetalles = cabecerasDetalles.length;
	var camposDetalles = [];
	html += "<table>";
	html += "<thead>";
	html += "<tr class='FilaCabecera'>";
	for(var j=0;j<nCamposDetalles;j++){			
		html += "<th style='width:";
		html += anchosDetalles[j];
		html += "'>";
		html += cabecerasDetalles[j];
		html += "</th>";
	}
	html += "</tr>";
	html += "</thead>";
	html += "<tbody>";
	for(var i=pos;i<nListaDetalles;i++){
		c++;
		camposDetalles = listaDetalles[i].split("|");
		if(camposDetalles[0]==idOrden){
			html += "<tr class='FilaDatos'>";
			for(var j=0;j<nCamposDetalles;j++){
				html += "<td>";
				html += camposDetalles[j];
				html += "</td>";
			}
			html += "</tr>";
		}
		else{
			pos = i;
			break;
		}
	}
	html += "</tbody>";
	html += "</table>";
	html += "</p>";
	return html;
}