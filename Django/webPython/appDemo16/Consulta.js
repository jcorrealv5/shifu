var listaOrdenes = [];
var listaDetalles = [];
var c=0;
var pos=3;

window.onload = function(){
	Validacion.ValidarNumerosEnlinea("N");
	
	btnImprimir.onclick = function(){
		Impresion.Imprimir(divReporte);
	}
	
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
	html += "<table>";
	html += "<thead>";
	html += "<tr class='FilaCabecera'>";
	for(var j=0;j<nCamposOrdenes;j++){			
		html += "<th style='width:";
		html += anchosOrdenes[j];
		html += "'>";
		html += "<div>";
		if(j==0) html += "<div id='cabExpandir' class='CabExpandir NoImprimir'>+</div>";
		html += cabecerasOrdenes[j];
		html += "</div>";		
		html += "</th>";
	}
	html += "</tr>";
	html += "</thead>";
	html += "<tbody>";
	for(var i=3;i<nListaOrdenes;i++){
		camposOrdenes = listaOrdenes[i].split("|");		
		html += "<tr class='FilaDatos'>";
		for(var j=0;j<nCamposOrdenes;j++){
			html += "<td><div>";
			if(j==0) {
				html += "<div class='Expandible NoImprimir' data-id='";
				html += camposOrdenes[0];
				html += "'>+</div>";
			}
			html += camposOrdenes[j];
			html += "</div></td>";
		}
		html += "</tr>";
		html += "<tr id='tr";
		html += camposOrdenes[0];
		html += "' style='display:none'>";
		html += "<td></td>";
		html += "<td colspan='";
		html += (nCamposOrdenes-1);
		html += "'>";
		html += crearTablaDetalles(camposOrdenes[0]);
		html += "</td>"
		html += "</tr>";		
	}
	html += "</tbody>";
	html += "</table>";
	divReporte.innerHTML = html;
	programarExpandirColapsar();
	var fin = new Date();
	var tiempo = fin - inicio;
	spnValida.innerText = "Ordenes: " + (nListaOrdenes-3) + " - Detalles: " + (nListaDetalles-3) + " - Bucles: " + c + " - Tiempo: " + tiempo + " msg";
}

function programarExpandirColapsar(){	
	var divs = document.getElementsByClassName("Expandible");
	var nDivs = divs.length;
	var div, id, fila;
	for(var i=0;i<nDivs;i++){
		div = divs[i];
		div.onclick = function(){
			id = this.getAttribute("data-id");
			fila = document.getElementById("tr" + id);
			if(this.innerText=="+"){
				fila.style.display = "table-row";
				this.innerText="-";
			}
			else{
				fila.style.display = "none";
				this.innerText="+";
			}
		}
	}
	
	var cabExpandir = document.getElementById("cabExpandir");
	cabExpandir.onclick = function(){
		if(cabExpandir.innerText=="+"){			
			for(var i=0;i<nDivs;i++){
				div = divs[i];
				id = div.getAttribute("data-id");
				fila = document.getElementById("tr" + id);
				fila.style.display = "table-row";
				div.innerText="-";
			}
			this.innerText="-";
		}
		else{
			for(var i=0;i<nDivs;i++){
				div = divs[i];
				id = div.getAttribute("data-id");
				fila = document.getElementById("tr" + id);
				fila.style.display = "none";
				div.innerText="+";
			}
			this.innerText="+";
		}
	}
}

function crearTablaDetalles(idOrden) {
	var html = "";
	var nListaDetalles = listaDetalles.length;
	var cabecerasDetalles = listaDetalles[0].split("|");
	var anchosDetalles = listaDetalles[1].split("|");
	var tiposDetalles = listaDetalles[2].split("|");
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
	var total = 0;
	var tipo = "";
	for(var i=pos;i<nListaDetalles;i++){
		c++;
		camposDetalles = listaDetalles[i].split("|");
		if(camposDetalles[0]==idOrden){
			html += "<tr class='FilaDatos'>";
			for(var j=0;j<nCamposDetalles;j++){
				tipo = tiposDetalles[j];
				html += "<td";
				if(tipo=="int" || tipo=="float"){
					html += " style='text-align:right'";
				}
				html += ">";
				html += camposDetalles[j];
				html += "</td>";
			}
			html += "</tr>";
			total += +camposDetalles[5];
		}
		else{
			pos = i;
			break;
		}
	}
	html += "</tbody>";
	html += "<tfoot>";
	html += "<tr class='FilaCabecera'>";
	for(var j=0;j<nCamposDetalles;j++){			
		html += "<th";
		if(j==(nCamposDetalles-1)) html += " style='text-align:right'";			
		html += ">";
		if(j==(nCamposDetalles-1)) html += total.toFixed(2);
		html += "</th>";
	}
	html += "</tr>";
	html += "</tfoot>";
	html += "</table>";
	return html;
}