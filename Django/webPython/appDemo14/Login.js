window.onload = function(){
	crearCaptcha();
	
	spnActualizarCaptcha.onclick = function(){
		crearCaptcha();
	}
	
	btnAceptar.onclick = async function(){
		if(Validacion.ValidarDatos("R", "N", spnValida)){
			var usuario = txtUsuario.value;
			var clave = txtClave.value;
			var claveCifrada = CryptoJS.SHA256(clave).toString();
			var codigo = txtCodigo.value;
			var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
			var frm = new FormData();
			frm.append("Usuario", usuario);
			frm.append("Clave", claveCifrada);
			frm.append("Codigo", codigo);
			frm.append("csrfmiddlewaretoken", token);
			var rptaHttp = await fetch("ValidarLogin", 
			{
				method: "POST",
				body: frm
			});
			if(rptaHttp.ok){
				var rpta = await rptaHttp.text();
				if(rpta!="") {
					if(!rpta.startsWith("Error")){
						var campos = rpta.split("|");
						sessionStorage.setItem("Usuario", usuario);
						sessionStorage.setItem("Cliente", rpta);
						alert("Bienvenido Empresa: " + campos[1]);
						window.location.href = "Categorias";
					}
					else alert(rpta);
				}
				else alert("Ocurrio un Error en el Servidor");
			}
		}	
	}
}

async function crearCaptcha(){
	var rptaHttp = await fetch("CrearCaptcha");
	if(rptaHttp.ok){
		var blob = await rptaHttp.blob();
		imgCaptcha.src = URL.createObjectURL(blob);
	}
}