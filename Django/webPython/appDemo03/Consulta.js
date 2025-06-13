window.onload = async function(){
	var rptaHttp = await fetch("ListarProductos");
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		divProducto.innerHTML = crearGrilla(rpta);
	}
}

function crearGrilla(rpta) {
    if (rpta != "") {
        var contenido = "<table><thead><tr class='FilaCabecera'>";
        var lista = rpta.split("¬");
		var cabecera = lista[0].split("|");
		var ancho = lista[1].split("|");
        var nRegistros = lista.length;
        var nCampos = cabecera.length;
        for (var j = 0; j < nCampos; j++) {
            contenido += "<th style='width:";
            contenido += ancho[j];
            contenido += "px'>";
            contenido += cabecera[j];
            contenido += "</th>";
        }
        contenido += "</tr></thead><tbody>";
        var campos;
        for (var i = 3; i < nRegistros; i++) {
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
        return contenido;
    }
}