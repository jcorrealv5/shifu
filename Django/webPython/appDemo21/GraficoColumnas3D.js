var ancho, alto, ctx;
var listaCategorias = [];
var nRegistros = 0;
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
		nRegistros = listaCategorias.length;
		Gui.Grilla(listaCategorias, divCategoria, "|", null, null,20, 10, ";");
	}
	calcularMaximoStock();
	graficar();
	
	btnDescargar.onclick = function(){
		var link = document.createElement("a");
		link.href = canvas.toDataURL();
		link.download = "GraficoColumnas2D.png";
		link.click();
	}
}

function dibujarTexto(texto, x, y, color, fuente){
	ctx.fillStyle=color;
	ctx.font = fuente;
	ctx.fillText(texto, x, y);
}

function dibujarBarra3D(x, y, ancho, alto, bordeAncho, bordeColor, colorRelleno, profundidad) {
    ctx.beginPath();
    if (bordeAncho != null) ctx.lineWidth = bordeAncho;
    if (bordeColor != null) ctx.strokeStyle = bordeColor;
    ctx.rect(x, y, ancho, alto);
    ctx.lineWidth = bordeAncho;
    ctx.strokeStyle = bordeColor;
    ctx.moveTo(x, y);
    ctx.lineTo(x + profundidad, y - profundidad);
    ctx.lineTo(x + ancho + profundidad, y - profundidad);
    ctx.lineTo(x + ancho + profundidad, y + alto - profundidad);
    ctx.lineTo(x + ancho, y + alto);
    ctx.moveTo(x + ancho + profundidad, y - profundidad);
    ctx.lineTo(x + ancho, y);
    ctx.stroke();
    if (colorRelleno != null) {
        ctx.fillStyle = colorRelleno;
        ctx.fill();
    }
    ctx.stroke();
    ctx.closePath();
}

function calcularMaximoStock(){
	maxStock = 0;
	var campos = [];
	var stock;
	for(var i=3;i<nRegistros;i++){
		campos = listaCategorias[i].split("|");
		stock = +campos[1];
		if(stock>maxStock) maxStock=stock;
	}	
}

function graficar(){
	ctx.fillStyle = "black";
	ctx.fillRect(0,0,ancho,alto);
	dibujarTexto("Grafico de Categorias", 300, 50, "yellow", "40px Arial");
	var campos = [];
	var stock, valor;
	var x = 50;
	var escalaV = (alto - 150) / maxStock;
	var anchoColumna = 50;
	var espaciado = 120;
	for(var i=3;i<nRegistros;i++){
		campos = listaCategorias[i].split("|");
		stock = +campos[1];
		valor = stock * escalaV;
		dibujarTexto(campos[0], x, alto - 30, "white", "15px Arial");
		var grad=ctx.createLinearGradient(0,0, anchoColumna,alto - 50 - valor);
		grad.addColorStop(0, "aqua");
		grad.addColorStop(1, "blue");
		dibujarBarra3D(x, alto - 50 - valor, anchoColumna, valor, 2, "yellow", grad, 5);
		dibujarTexto(campos[1], x + 10, alto - 70 - valor, "white", "15px Arial");
		x += espaciado;
	}
}