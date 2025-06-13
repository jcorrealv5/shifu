var ancho, alto, ctx;
var listaCategorias = [];
var maxStock = 0;
var escalaH = 0;

var nRegistros = 0;
var cRegistros = 3;
var cX = 0;
var y = 100;
var idAnimacion = null;

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
	idAnimacion = requestAnimationFrame(graficar);
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
	escalaH = (ancho - 250) / maxStock;
}

function graficar(){
	ctx.fillStyle = "black";
	ctx.fillRect(0,0,ancho,alto);
	dibujarTexto("Grafico de Categorias", 300, 50, "yellow", "40px Arial");
	var campos = [];
	var stock, valor;
	campos = listaCategorias[cRegistros].split("|");
	stock = +campos[1];
	valor = stock * escalaH;
	if(cRegistros>3){
		var posY = 100;
		var subcampos = [];
		var subStock, subValor;
		for(var i=3;i<cRegistros;i++){
			subcampos = listaCategorias[i].split("|");
			subStock = +subcampos[1];
			subValor = subStock * escalaH;
			dibujarTexto(subcampos[0], 20, posY, "white", "15px Arial");
			var grad=ctx.createLinearGradient(0,0, subValor,30);
			grad.addColorStop(0, "aqua");
			grad.addColorStop(1, "blue");
			//ctx.fillStyle = grad;
			//ctx.fillRect(150, posY-20, subValor, 30);
			dibujarBarra3D(150, posY-20, subValor, 30, 2, "yellow", grad, 5);
			dibujarTexto(subcampos[1], 170 + subValor, posY, "white", "15px Arial");
			posY += 50;
		}
	}
	dibujarTexto(campos[0], 20, y, "white", "15px Arial");
	var grad=ctx.createLinearGradient(0,0, cX,30);
	grad.addColorStop(0, "aqua");
	grad.addColorStop(1, "blue");
	//ctx.fillStyle = grad;
	//ctx.fillRect(150, y-20, cX, 30);
	dibujarBarra3D(150, y-20, cX, 30, 2, "yellow", grad, 5);
	dibujarTexto(campos[1], 170 + cX, y, "white", "15px Arial");
	if(cX<valor) cX++;
	else {
		cX = 0;
		y += 50;
		if(cRegistros<nRegistros-1) cRegistros++;
		else {
			y = 100;
			cRegistros=3;
		}
	}
	idAnimacion = requestAnimationFrame(graficar);
}