var grupoTotal = 0;
var grupoContador = 0;
var diccionario = {};
var nArchivos;
var cArchivos = 0;

window.onload = function(){
	btnConsultar.onclick = async function(){
		divProgreso.style.display="inline";
		pbrConsulta.value = 0;
		divRpta.innerHTML = "";
		var rptaHttp = await fetch("ListarArchivos");
		if(rptaHttp.ok){
			var data = await rptaHttp.text();
			var listaArchivos = data.split(";");
			nArchivos = listaArchivos.length;
			var campos = [];
			var total = 0;
			var limite = 100 * 1024; //100 KB
			var nombres = [];
			var c = 0;
			for(var i=0;i<nArchivos;i++) {
				campos = listaArchivos[i].split("|");
				nombre = campos[0];
				size = +campos[1];
				total += size;
				if(total<limite){
					nombres.push(nombre);
				}
				else{
					c=c+1;
					diccionario[c.toString()] = nombres;
					nombres = [];
					nombres.push(nombre);
					total = 0;
				}
			}
			if(nombres.length>0) {
				c=c+1;
				diccionario[c.toString()] = nombres;
			}
			// console.log("x: " + x);
			console.log(diccionario);
			grupoTotal = c;
			grupoContador = 0;
			pbrConsulta.max = c;
			cArchivos = 0;
			await obtenerImagenes();
		}
	}
}

async function obtenerImagenes(){
	var data = (diccionario[(grupoContador + 1).toString()]).join("|");
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
	var frm = new URLSearchParams();
	frm.append("Archivos", data);
	frm.append("csrfmiddlewaretoken", token);
	var rptaHttp = await fetch("ObtenerImagenes",
	{
		method: "POST",
		headers: {"Content-Type": "application/x-www-form-urlencoded",},
		body: frm
	});
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
			var sizes = texto.split("|");
			var nImagenes = sizes.length;
			cArchivos += nImagenes;
			var x = 1+nTexto;
			var bytesImagen;
			var img;
			for(var i=0;i<nImagenes;i++){
				size = +sizes[i];
				bytesImagen = blob.slice(x, x + size);
				var blobImagen = new Blob([bytesImagen], { "type": "image/jpg" });
				img = new Image(200,200);
				img.src = URL.createObjectURL(blobImagen);
				divRpta.appendChild(img);
				x += size;
			}
		}
		grupoContador++;
		spnMensaje.innerText = "Cargando: " + cArchivos + " de " + nArchivos;
		pbrConsulta.value++;
		if(grupoContador<grupoTotal){
			await obtenerImagenes();
		}
	}
}