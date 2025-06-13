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
	var html = "<rect x='0' y='0' width='";
	html += ancho;
	html += "' height='";
	html += alto;
	html += "' fill='grey'>";
	html += "</rect>";	
	html += "<text x='300' y='50' fill='pink' style='font:40px arial'>Grafico de Categorias</text>";
	var nRegistros = listaCategorias.length;
	var y = 100;
	var campos = [];
	var escalaH = (ancho - 250) / maxStock;
	var stock, valor;
	for(var i=3;i<nRegistros;i++){
		campos = listaCategorias[i].split("|");
		stock = +campos[1];
		valor = stock * escalaH;
		html += "<text x='20' y='";
		html += y;
		html += "' fill='white' style='font:15px arial'>";
		html += campos[0];
		html += "</text>";
		html += "<defs>";
		html += "<linearGradient id='deg' x1='0%' x2='0%' y1='0%' y2='100%'>";
		html += "<stop offset='0%' stop-color='yellow'/>";
		html += "<stop offset='100%' stop-color='brown'/>";
		html += "</linearGradient>";
		html += "</defs>";
		html += "<rect x='150' y='"
		html += y-20;
		html += "' width='";
		html += valor;
		html += "' height='30' fill='url(#deg)'>";
		html += "</rect>";
		html += "<text x='";
		html += 170 + valor
		html += "' y='";
		html += y;
		html += "' fill='white' style='font:15px arial'>";
		html += campos[1];
		html += "</text>";
		y += 50;
	}	
	svg.innerHTML = html;
}