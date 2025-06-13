var listaTablas = [];
var ultimoBoton = null;

window.onload = async function(){
	var rptaHttp = await fetch("ObtenerListas");
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		var listas = rpta.split("_");
		var listaNombres = listas[0].split("|");		
		var nTablas = listas.length;
		for(var i=1;i<nTablas;i++){
			listaTablas.push(listas[i].split("¬"));
		}
		var html = "";
		var nTabs = listaNombres.length;
		html += "<div>";
		for(var i=0;i<nTabs;i++){
			html += "<input type='button' class='Boton' value='";
			html += listaNombres[i];
			html += "' data-id='";
			html += i;
			html += "'/>";
		}
		html += "</div>";
		html += "<div id='divData'></div>";
		divConsulta.innerHTML = html;
		programarTabs();
		var botones = document.getElementsByClassName("Boton");
		botones[0].click();
	}
}

function programarTabs(){
	var botones = document.getElementsByClassName("Boton");
	var nBotones = botones.length;
	for(var i=0;i<nBotones;i++){				
		botones[i].onclick = function(){
			if(ultimoBoton!=null) ultimoBoton.className = "Boton";	
			this.className = "BotonActivo";
			var id = this.getAttribute("data-id");
			var lista = listaTablas[id];
			var divData = document.getElementById("divData");
			Gui.Grilla(lista, divData, "|", null, null,20, 10, "¬");
			ultimoBoton = this;
		}
	}
}