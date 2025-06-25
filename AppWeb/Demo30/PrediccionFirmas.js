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
			grosor = 6;
			ctx.fillStyle="white";
			ctx.fillRect(x-grosor,y-grosor,2*grosor,2*grosor);
		}
	}
	
	btnPredecir.onclick = async function(){
		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
		var frm = new FormData();
		var firma = canvas.toDataURL().replace("data:image/png;base64,","");
		frm.append("Firma", firma);
		frm.append("csrfmiddlewaretoken", token);
		var rptaHttp = await fetch("PredecirFirma", 
		{
			method: "POST",
			body: frm
		});
		if(rptaHttp.ok){
			var rptaFirma = await rptaHttp.text();
			spnUsuario.innerText = rptaFirma;
		}
	}
	
	btnNuevo.onclick = function(){
		ctx.fillStyle="black";
		ctx.fillRect(0,0,ancho,alto);
		spnUsuario.innerText = "";
	}
}