window.onload = function(){
	var ctx = canvas.getContext("2d");
	var ancho = canvas.width;
	var alto = canvas.height;
	ctx.fillStyle="black";
	ctx.fillRect(0,0,ancho,alto);	
	var esDibujo = false;
	
	canvas.onmousedown = function(){		
		esDibujo = !esDibujo;
	}
	canvas.onmousemove = function(event){
		if(esDibujo){
			var x = event.offsetX;
			var y = event.offsetY;
			grosor = 20;
			ctx.fillStyle="white";
			ctx.fillRect(x-grosor,y-grosor,2*grosor,2*grosor);
		}
	}
	
	btnClasificar.onclick = async function(){
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var frm = new FormData();
		var digito = canvas.toDataURL().replace("data:image/png;base64,","");
		frm.append("Digito", digito);
		frm.append("csrfmiddlewaretoken", token);
		var rptaHttp = await fetch("ClasificarDigito", 
		{
			method: "POST",
			body: frm
		});
		if(rptaHttp.ok){
			var rptaDigito = await rptaHttp.text();
			divDigito.innerHTML = rptaDigito;
		}
	}
	
	btnNuevo.onclick = function(){
		ctx.fillStyle="black";
		ctx.fillRect(0,0,ancho,alto);
		divDigito.innerHTML = "";
	}
}