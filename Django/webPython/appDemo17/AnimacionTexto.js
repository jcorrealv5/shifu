var ancho, alto, ctx, posX, mensaje;
var idAnimacion;

window.onload = function(){
	ancho = canvas.width;
	alto = canvas.height;
	ctx = canvas.getContext("2d");
	ctx.fillStyle = "black";
	ctx.fillRect(0,0,ancho,alto);
	posX=-400;
	reconocimientoVoz();
	
	btnAnimar.onclick = function(){
		mensaje = txtMensaje.value;
		if(this.value=="Animar")
		{
			this.value="Detener";
			idAnimacion = requestAnimationFrame(animarTexto);			
		}
		else{
			this.value="Animar";
			cancelAnimationFrame(idAnimacion);
		}
	}
}

function animarTexto(){
	ctx.fillStyle = "black";
	ctx.fillRect(0,0,ancho,alto);
	ctx.fillStyle = "white";
	ctx.font = "100px Arial";
	ctx.fillText(mensaje,posX,300);
	if(posX<ancho) posX += 10;
	else posX=-400;
	idAnimacion = requestAnimationFrame(animarTexto);
}

function ejecutarComandoVoz(palabras, comando){
	mensaje = txtMensaje.value;
	if(comando=="animar")
	{
		this.value="Detener";
		idAnimacion = requestAnimationFrame(animarTexto);			
	}
	else if(comando=="detener"){
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