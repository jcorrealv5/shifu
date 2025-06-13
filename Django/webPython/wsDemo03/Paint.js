var ws = null;
var esModoDibujo=false;
var ctx = null;
var color;

window.onload = function(){
	ctx = canvas.getContext("2d");
	ctx.fillStyle="white";
	ctx.fillRect(0,0,canvas.width,canvas.height);
	
	canvas.onmousedown = function(){
		color = txtColor.value;
		esModoDibujo = !esModoDibujo;
	}
	
	canvas.onmousemove= function(event){
		if(esModoDibujo){
			var x = event.offsetX;
			var y = event.offsetY;						
			var mensaje = color;
			mensaje += "|";
			mensaje += x;
			mensaje += "|";
			mensaje += y;
			if(ws!=null) ws.send(mensaje);
		}
	}
	
	btnLimpiar.onclick = function(){
		ctx.fillStyle="white";
		ctx.fillRect(0,0,canvas.width,canvas.height);
	}
	
	ws = new WebSocket("ws://190.43.83.241:9002")
	ws.onopen = function(){
		spnEstado.innerText = "Conectado";
	}
	ws.onclose = function(){
		spnEstado.innerText = "Desconectado";
	}
	ws.onmessage = function(event){
		spnEstado.innerText = "Recibiendo";
		setTimeout(function() { spnEstado.innerText = "Conectado"; }, 5000);
		var data = event.data;
		if(data!=""){
			var campos = data.split("|");
			var x = +campos[1];
			var y = +campos[2];
			ctx.fillStyle = campos[0];
			ctx.fillRect(x-5,y-5,10,10);
		}
	}
}