var ancho, alto;
var listaCategorias = [];
var maxStock = 0;

window.onload = async function(){
	ancho = svg.width.baseVal.value;
	alto = svg.height.baseVal.value;	
	
	var rptaHttp = await fetch("ConsultarStockProductos");
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		listaCategorias = rpta.split(";");
		Gui.Grilla(listaCategorias, divCategoria, "|", null, null,20, 10, ";");
	}
	calcularMaximoStock();
	graficarCategorias();
	
	btnDescargar.onclick = function(){
		var blob = new Blob([svg.outerHTML], {"type":"text/plain"});
        var link = document.createElement("a");
        link.download = "Grafico de Categorias.svg";
        link.href = URL.createObjectURL(blob);
        link.click();
	}
}

function calcularMaximoStock(){
	var nRegistros = listaCategorias.length;
	maxStock = 0;
	var campos = [];
	var stock;
	for(var i=3;i<nRegistros;i++){
		campos = listaCategorias[i].split("|");
		stock = +campos[1];
		if(stock>maxStock) maxStock=stock;
	}
}

function graficarCategorias(){
	var html = SVG.crearRectangulo("fondo", "", "", 0, 0, ancho, alto, "black", "", "", 0, null);
	html += "<defs>";
	html += "<linearGradient id='deg' x1='0%' x2='0%' y1='0%' y2='100%'>";
	html += "<stop offset='0%' stop-color='aqua'/>";
	html += "<stop offset='100%' stop-color='blue'/>";
	html += "</linearGradient>";
	html += "</defs>";
	html += SVG.crearTexto(300, 50, 'yellow', 'arial', 40, 'Grafico de Categorias', null);
	var nRegistros = listaCategorias.length;
	var y = 100;
	var campos = [];
	var escalaH = (ancho - 250) / maxStock;
	var stock, valor;
	for(var i=3;i<nRegistros;i++){
		campos = listaCategorias[i].split("|");
		stock = +campos[1];
		valor = stock * escalaH;
		html += SVG.crearTexto(20, y, 'white', 'arial', 15, campos[0], null);
		html += SVG.crearRectangulo("barra" + i, "", "", 150, y-20, valor, 30, "url(#deg)", "blue", 1, 10, null);
		html += SVG.crearTexto(170 + valor, y, 'white', 'arial', 15, campos[1], null);
		y += 50;
	}	
	svg.innerHTML = html;
}