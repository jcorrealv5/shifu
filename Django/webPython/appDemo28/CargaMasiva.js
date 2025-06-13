var file = null;
var tabla = "";
var lista = [];

var totalRegistros = 0;
var registrosBloque = 0;
var totalViajes = 0;
var contadorViajes = 0;
var contadorRegistros = 0;

window.onload = function(){
	btnAbrir.onclick = function(){
		fupArchivo.click();
	}
	
	btnGrabar.onclick = async function(){
		horaInicio = new Date();
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var frm = new FormData();
		frm.append("tabla", tabla);
		frm.append("campos", lista[0]);
		frm.append("csrfmiddlewaretoken", token);
		var rptaHttp = await fetch("ValidarTablaCampos", 
		{
			method: "POST",
			body: frm
		});
		if(rptaHttp.ok){
			var rptaTexto = await rptaHttp.text();
			if(rptaTexto!="")
			{
				alert(rptaTexto);
			}
			else{				
				grabarBloqueRegistros();
			}
		}
	}
	
	fupArchivo.onchange = function(){
		file = this.files[0];
		tabla = file.name.split(".")[0];
		txtArchivo.value = file.name;
		var reader = new FileReader();
		reader.onloadend = function(){
			var data = reader.result;
			lista = data.split("\r\n");
			var campos = lista[0].split(",");
			var nCampos = campos.length;
			var anchos = "";
			var tipos = "";
			for(var i=0;i<nCampos;i++) {
				if(i==0) anchos += "80";
				else anchos += "200";
				tipos += "str";
				if(i<nCampos-1){
					anchos += ","
					tipos += ","
				}
			}
			lista.splice(1, 0, anchos);
			lista.splice(2, 0, tipos);
			Gui.Grilla(lista, divData, ",", null, null, 20, 10, "\r\n", "", false, false, "", false, false, false, null, null, null);
			iniciarVariables();
		}
		reader.readAsText(file, "ISO-8859-1");
	}
}

function iniciarVariables(){
	totalRegistros = lista.length - 3;
	registrosBloque = +txtRegistrosBloque.value;
	totalViajes = Math.floor(totalRegistros/ registrosBloque);
	if(totalRegistros % registrosBloque > 0) totalViajes++;
	contadorViajes = 0;
	contadorRegistros = 0;
	progreso.value = 0;
	progreso.max = totalViajes;
	spnRegistros.innerText = "Total Registros: " + totalRegistros;
	spnBloques.innerText = "Total Viajes: " + totalViajes;
	spnProgresoRegistros.innerText = "";
	spnProgresoBloques.innerText = "";	
}

async function grabarBloqueRegistros(){
	var listaBloque = [];
	listaBloque.push(lista[0]);
	var inicio = (contadorViajes * registrosBloque) + 3;
	var fin = inicio + registrosBloque;
	for(var i=inicio;i<fin;i++) {
		if(i<totalRegistros+3){
			contadorRegistros++;
			listaBloque.push(lista[i]);
		}
		else break;
	}
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
	var data = listaBloque.join(";")
	var frm = new FormData();
	frm.append("tabla", tabla);
	frm.append("data", data);
	frm.append("csrfmiddlewaretoken", token);
	var rptaHttp = await fetch("GrabarBloqueRegistros", 
	{
		method: "POST",
		body: frm
	});
	if(rptaHttp.ok){
		var rptaTexto = await rptaHttp.text();
		if(rptaTexto=="OK")
		{
			contadorViajes++;
			progreso.value = contadorViajes;
			spnProgresoRegistros.innerText = "Registros Grabados: " + contadorRegistros;
			spnProgresoBloques.innerText = "Cantidad Viajes: " + contadorViajes;
			if(contadorViajes<totalViajes){
				grabarBloqueRegistros();
			}
			else{
				alert("Se grabo todos los registros en la tabla: " + tabla);
			}
		}
		else{
			alert(rptaTexto);
		}
	}
}

function seleccionarFila(idGrilla, fila, idReg){
}