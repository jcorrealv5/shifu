window.onload = function(){
	btnConsultar.onclick = async function(){
		var tipo = cboTipo.value;
		var rptaHttp = await fetch("ConsultarProductos?id=" + txtCodigo.value + "&tipo=" + tipo);
		if(rptaHttp.ok){
			var rpta = await rptaHttp.text();
			if(rpta!=""){
				if(!rpta.startsWith("Error")){
					if(tipo=="csv"){
						var lista = rpta.split("¬");
						crearTablaCsv(lista, divProducto, spnMensaje);
					}
					else if(tipo=="json"){
						var lista = JSON.parse(rpta);					
						crearTablaJson(lista, divProducto, spnMensaje);
					}
					else if(tipo=="xml"){
						parser = new DOMParser();
						var docXml = parser.parseFromString(rpta,"text/xml");										
						crearTablaXml(docXml, divProducto, spnMensaje);						
					}
				}
				else alert(rpta);
			}
			else alert("Ocurrio un error en la llamada al Servicio");
		}
	}
}

function crearTablaCsv(lista, div, spn) {
    var campos = lista[0].split("|");
    var nRegistros = lista.length;
    var fila;
    var nCampos = campos.length;
    var col;
    var contenido = "<table><thead><tr class='FilaCabecera'>";
    for (var j = 0; j < nCampos; j++) {
        col = campos[j];
        contenido += "<th>";
        contenido += col;
        contenido += "</th>";
    }
    contenido += "</tr></thead><tbody>";
    for (var i = 1; i < nRegistros; i++) {
        campos = lista[i].split("|");
        contenido += "<tr class='FilaDatos'>";
        for (var j = 0; j < nCampos; j++) {
            contenido += "<td>";
            contenido += campos[j];
            contenido += "</td>";
        }
        contenido += "</tr>";
    }
    contenido += "</tbody></table>";
    div.innerHTML = contenido;
    spn.innerHTML = nRegistros;
}

function crearTablaJson(json, div, spn) {
    var campos = Object.keys(json[0]);
    var nRegistros = json.length;
    var fila;
    var nCampos = campos.length;
    var col;
    var contenido = "<table><thead><tr class='FilaCabecera'>";
    for (var j = 0; j < nCampos; j++) {
        col = campos[j];
        contenido += "<th>";
        contenido += col;
        contenido += "</th>";
    }
    contenido += "</tr></thead><tbody>";
    for (var i = 0; i < nRegistros; i++) {
        fila = json[i];
        contenido += "<tr class='FilaDatos'>";
        for (var j = 0; j < nCampos; j++) {
            col = fila[campos[j]];
            contenido += "<td>";
            contenido += col;
            contenido += "</td>";
        }
        contenido += "</tr>";
    }
    contenido += "</tbody></table>";
    div.innerHTML = contenido;
    spn.innerHTML = nRegistros;
}

function crearTablaXml(docXml, div, spn) {
    nodosCampos = docXml.firstChild.firstChild.childNodes;
	var nCampos = nodosCampos.length;
	var campos = [];
	for(var j=0;j<nCampos;j++){
		campos.push(nodosCampos[j].nodeName);
	}
    var nRegistros = docXml.firstChild.childNodes.length;
    var fila;
    var nCampos = campos.length;
    var col;
    var contenido = "<table><thead><tr class='FilaCabecera'>";
    for (var j = 0; j < nCampos; j++) {
        col = campos[j];
        contenido += "<th>";
        contenido += col;
        contenido += "</th>";
    }
    contenido += "</tr></thead><tbody>";
    for (var i = 0; i < nRegistros; i++) {
        nodoCampos = docXml.firstChild.childNodes[i].childNodes;
        contenido += "<tr class='FilaDatos'>";
        for (var j = 0; j < nCampos; j++) {			
            col = nodoCampos[j].firstChild.nodeValue;
            contenido += "<td>";
            contenido += col;
            contenido += "</td>";
        }
        contenido += "</tr>";
    }
    contenido += "</tbody></table>";
    div.innerHTML = contenido;
    spn.innerHTML = nRegistros;
}