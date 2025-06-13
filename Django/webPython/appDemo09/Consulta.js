var grupoTotal = 0;
var grupoContador = 0;
var diccionario = {};
var nArchivos;
var cArchivos = 0;
var imagenBlobs = [];
var imagenTotalPaginas = 0;
var imagenContadorPaginas = 0;
var imagenCantidadPagina = 10;

window.onload = function(){
	programarBotones();
	
	cboPagina.onchange = function(){
		imagenContadorPaginas = this.value;
		mostrarImagenes();
	}
	
	btnConsultar.onclick = async function(){	
		divProgreso.style.display="inline";
		pbrConsulta.value = 0;
		divRpta.innerHTML = "";
		var rptaHttp = await fetch("ListarArchivos");
		if(rptaHttp.ok){
			var data = await rptaHttp.text();
			var listaArchivos = data.split(";");
			nArchivos = listaArchivos.length;
			imagenTotalPaginas = Math.floor(nArchivos / imagenCantidadPagina);
			if(nArchivos % imagenCantidadPagina > 0) imagenTotalPaginas++;
			var html = "";
			for(var i=0;i<imagenTotalPaginas;i++){
				html += "<option value='";
				html += i;
				html += "'>";
				html += (i+1);
				html += "</option>";
			}
			cboPagina.innerHTML = html;
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
				imagenBlobs.push(blobImagen);
				x += size;
			}					
		}
		grupoContador++;
		if(grupoContador==1) mostrarImagenes();
		spnMensaje.innerText = "Cargando: " + cArchivos + " de " + nArchivos;
		pbrConsulta.value++;
		if(grupoContador<grupoTotal){
			await obtenerImagenes();
		}
	}
}

function mostrarImagenes(){
	divRpta.innerHTML = "";
	var inicio = imagenContadorPaginas * imagenCantidadPagina;
	var fin = inicio + imagenCantidadPagina;
	var blobImagen;
	for(var i=inicio;i<fin;i++){
		if(i<nArchivos){
			blobImagen = imagenBlobs[i];
			img = new Image(200,200);
			img.src = URL.createObjectURL(blobImagen);
			divRpta.appendChild(img);
		}
		else break;
	}
	txtTotalPaginas.value = imagenTotalPaginas;
	cboPagina.value = imagenContadorPaginas;
}

function programarBotones(){
	var botones = document.getElementsByClassName("BotonSmall");
	var nBotones = botones.length;
	for(var i=0;i<nBotones;i++){
		botones[i].onclick = function(){
			var pos = this.getAttribute("data-pos");
			if(pos==-1){
				imagenContadorPaginas = 0;
			}
			else if(pos==-2){
				if(imagenContadorPaginas>0) imagenContadorPaginas--;
			}
			else if(pos==-3){
				if(imagenContadorPaginas<imagenTotalPaginas-1) imagenContadorPaginas++;
			}
			else if(pos==-4){
				imagenContadorPaginas = imagenTotalPaginas-1;
			}
			mostrarImagenes();
		}
	}
}