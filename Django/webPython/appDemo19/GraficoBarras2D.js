var ancho, alto, ctx;
var listaCategorias = [];
var maxStock = 0;

window.onload = async function(){
	ancho = canvas.width;
	alto = canvas.height;
	ctx = canvas.getContext("2d");
	ctx.fillStyle = "black";
	ctx.fillRect(0,0,ancho,alto);
	
	var rptaHttp = await fetch("ConsultarStockProductos");
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		listaCategorias = rpta.split(";");
		Gui.Grilla(listaCategorias, divCategoria, "|", null, null,20, 10, ";");
	}
	calcularMaximoStock();
	graficarCategorias();
	
	btnDescargar.onclick = function(){
		var link = document.createElement("a");
		link.href = canvas.toDataURL();
		link.download = "GraficoBarras2D.png";
		link.click();
	}
}

function dibujarTexto(texto, x, y, color, fuente){
	ctx.fillStyle=color;
	ctx.font = fuente;
	ctx.fillText(texto, x, y);
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
	dibujarTexto("Grafico de Categorias", 300, 50, "yellow", "40px Arial");
	var nRegistros = listaCategorias.length;
	var y = 100;
	var campos = [];
	var escalaH = (ancho - 250) / maxStock;
	var stock, valor;
	for(var i=3;i<nRegistros;i++){
		campos = listaCategorias[i].split("|");
		stock = +campos[1];
		valor = stock * escalaH;
		dibujarTexto(campos[0], 20, y, "white", "15px Arial");
		var grad=ctx.createLinearGradient(0,0, valor,30);
		grad.addColorStop(0, "aqua");
		grad.addColorStop(1, "blue");
		ctx.fillStyle = grad;
		ctx.fillRect(150, y-20, valor, 30);
		dibujarTexto(campos[1], 170 + valor, y, "white", "15px Arial");
		y += 50;
	}
}