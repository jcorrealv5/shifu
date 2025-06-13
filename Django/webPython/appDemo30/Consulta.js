window.onload = function(){
	btnConsultar.onclick = async function(){
		var rptaHttp = await fetch("ConsultarProductos?id=" + txtCodigo.value);
		if(rptaHttp.ok){
			var rpta = await rptaHttp.text();
			if(rpta!=""){
				if(!rpta.startsWith("Error")){
					var lista = JSON.parse(rpta);
					console.log(lista);
					crearTablaJson(lista, divProducto, spnMensaje);
				}
				else alert(rpta);
			}
			else alert("Ocurrio un error en la llamada al Servicio");
		}
	}
}

function crearTablaJson(json, div, spn) {
    var campos = Object.keys(json[0]);
	console.log(campos);
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