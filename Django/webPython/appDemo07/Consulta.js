window.onload = function(){
	btnConsultar.onclick = async function(){
		var id = txtCodigo.value;
		var rptaHttp = await fetch("ConsultarAlumno?id=" + id);
		if(rptaHttp.ok){
			var blob = await rptaHttp.blob();
			var nTotal = blob.size;
			if(nTotal>0){
				//Obtener el tamanio del Texto
				var byte1 = blob.slice(0, 1);
				var buffer1 = await byte1.arrayBuffer();
				var array1 = new Uint8Array(buffer1);
				var nTexto = array1[0];
				//Obtener el Texto
				var bytesTexto = blob.slice(1, 1 + nTexto);
				var bufferTexto = await bytesTexto.arrayBuffer();
				var arrayTexto = new Uint8Array(bufferTexto);
				var texto = "";
				for(var i=0;i<nTexto;i++){
					texto += String.fromCharCode(arrayTexto[i]);
				}
				//Mostrar en los controles
				var campos = texto.split("|");
				txtApellidos.value = campos[0];
				txtNombres.value = campos[1];
				txtCorreo.value = campos[2];
				//Obtener la imagen
				var bytesImagen = blob.slice(1+nTexto, nTotal);	
				console.log(bytesImagen);
				var blobImagen = new Blob([bytesImagen], { "type": "image/jpg" });
				imgFoto.src = URL.createObjectURL(blobImagen);				
			}
			else{
				txtApellidos.value = "";
				txtNombres.value = "";
				txtCorreo.value = "";
				imgFoto.src = "";
				alert("No existe el Codigo");
			}
		}
	}
}