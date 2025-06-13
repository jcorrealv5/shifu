var ws = null;
window.onload = function(){
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
		var campos = data.split("|");
		var mensaje = campos[0];
		mensaje += "<br/>";
		mensaje += campos[1];
		mensaje += " dice:<br/>";
		mensaje += campos[2];
		mensaje += "<br/><hr/>"
		divPanel.insertAdjacentHTML("afterbegin", mensaje); 
	}
	btnEnviar.onclick = async function(){
		if(ws!=null) {
			var mensaje = new Date();
			mensaje += "|";
			mensaje += txtUsuario.value;
			mensaje += "|";
			mensaje += txtMensaje.value;
			ws.send(mensaje);
		}
	}
}