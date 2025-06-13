var ancho, alto, ctx, posX, x, y, cx, cy;
var idAnimacion;

window.onload = function(){
	anchoSprite = 1500;
	altoSprite = 710;
	numCols = 4;
	numFilas = 3;
	
	anchoImagen = Math.floor(anchoSprite / numCols);
	altoImagen = Math.floor(altoSprite / numFilas);
	
	ancho = canvas.width;
	alto = canvas.height;
	ctx = canvas.getContext("2d");
	ctx.fillStyle = "white";
	ctx.fillRect(0,0,ancho,alto);
	posX=-anchoImagen;
	x = 0;
	y = 0;
	cx = 0;
	cy = 0;
	reconocimientoVoz();
	
	btnAnimar.onclick = function(){
		if(this.value=="Animar")
		{
			this.value="Detener";
			idAnimacion = requestAnimationFrame(animarImagen);			
		}
		else{
			this.value="Animar";
			cancelAnimationFrame(idAnimacion);
		}
	}
}

function animarImagen(){
	ctx.fillStyle = "white";
	ctx.fillRect(0,0,ancho,alto);	
	ctx.drawImage(imgSprite, x, y, anchoImagen, altoImagen, posX, 200, anchoImagen, altoImagen);
	cx++;
	if(cx<numCols){
		x += anchoImagen;
	}
	else{
		cx=0;
		x=0;
		cy++;
		if(cy<numFilas) y += altoImagen;
		else {
			cy = 0;
			y =0;
		}
	}	
	if(posX<ancho) posX += 10;
	else posX=-anchoImagen;
	idAnimacion = requestAnimationFrame(animarImagen);
}

function ejecutarComandoVoz(palabras, comando){
	comando = comando.toLowerCase();
	if(comando=="animar")
	{
		this.value="Detener";
		idAnimacion = requestAnimationFrame(animarImagen);			
	}
	else if(comando=="detener" || comando=="stop"){
		this.value="Animar";
		cancelAnimationFrame(idAnimacion);
	}
}

function reconocimientoVoz() {
    if ('webkitSpeechRecognition' in window) {
        var recognizing = false;
        var recognition = new webkitSpeechRecognition();
        recognition.continuous = true;
        recognition.interimResults = false;
        iniciarReconocimiento();

        recognition.onresult = function (event) {
            var palabras = event.results[event.results.length - 1][0].transcript.trim();
            var palabra = palabras.split(" ");
            var comando = "";
            if (palabra.length > 0) {
                comando = palabra[0];
                var spnComando = document.getElementById("spnComando");
                if (spnComando != null) spnComando.innerHTML = palabras;
            }
            ultimoComando = comando;
            ejecutarComandoVoz(palabras, comando);
        };

        recognition.onstart = function () {
            //alert("Iniciando Reconocimiento");
            recognizing = true;
        };

        recognition.onend = function () {
            //alert("Finalizando Reconocimiento");
            recognizing = false;
        };

        recognition.onerror = function (event) {
            alert(event.error);
        };

        function iniciarReconocimiento() {
            if (recognizing) {
                recognition.stop();
                return;
            }
            recognition.lang = "es-PE";
            recognition.start();
        }
    }
}