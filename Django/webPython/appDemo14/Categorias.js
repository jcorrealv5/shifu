var grupoTotal = 0;
var grupoContador = 0;
var diccionario = {};
var nArchivos;
var cArchivos = 0;
var imagenBlobs = [];
var imagenTotalPaginas = 0;
var imagenContadorPaginas = 0;
var imagenCantidadPagina = 8;
var listaCategorias = [];
var soloUnaVez = true;

window.onload = function(){
	programarBotones();
	
	cboPagina.onchange = function(){
		imagenContadorPaginas = this.value;
		mostrarDataConImagenes();
	}
	
	listarCategorias();
}

async function listarCategorias(){	
	divProgreso.style.display="inline";
	pbrConsulta.value = 0;
	divRpta.innerHTML = "";
	var rptaHttp = await fetch("ListarCodigos?Carpeta=Categoria");
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
		var codigos = [];
		var c = 0;
		for(var i=0;i<nArchivos;i++) {
			campos = listaArchivos[i].split("|");
			codigo = campos[0];
			size = +campos[1];
			total += size;
			if(total<limite){
				codigos.push(codigo);
			}
			else{
				c=c+1;
				diccionario[c.toString()] = codigos;
				codigos = [];
				codigos.push(codigo);
				total = 0;
			}
		}
		if(codigos.length>0) {
			c=c+1;
			diccionario[c.toString()] = codigos;
		}
		grupoTotal = c;
		grupoContador = 0;
		pbrConsulta.max = c;
		cArchivos = 0;
		await obtenerDataImagenes();
	}
}

async function obtenerDataImagenes(){
	var data = (diccionario[(grupoContador + 1).toString()]).join("|");
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
	var frm = new FormData();
	frm.append("Carpeta", "Categoria");
	frm.append("Codigos", data);
	frm.append("csrfmiddlewaretoken", token);
	var rptaHttp = await fetch("ObtenerImagenes", 
	{
		method: "POST",
		body: frm
	});
	if(rptaHttp.ok){
		var blob = await rptaHttp.blob();
		var nTotal = blob.size;		
		if(nTotal>0){
			//Obtener el Byte 1
			var byte1 = blob.slice(0, 1);
			var buffer1 = await byte1.arrayBuffer();
			var array1 = new Uint8Array(buffer1);
			var n1 = array1[0];
			//Obtener el Byte 2
			var byte2 = blob.slice(1, 2);
			var buffer2 = await byte2.arrayBuffer();
			var array2 = new Uint8Array(buffer2);
			var n2 = array2[0];
			//Obtener el Tamanio del Texto
			var nTexto = (n1 * 255) + n2
			//Obtener el Texto
			var bytesTexto = blob.slice(2, 2 + nTexto);
			var bufferTexto = await bytesTexto.arrayBuffer();
			var arrayTexto = new Uint8Array(bufferTexto);
			var texto = "";
			for(var i=0;i<nTexto;i++){
				texto += String.fromCharCode(arrayTexto[i]);
			}
			var lista = texto.split(";")
			var nRegistros = lista.length;		
			var sizes = [];			
			var x = 2+nTexto;
			var campos = [];
			var size,bytesImagen,img;
			for(var i=0;i<nRegistros;i++){
				campos = lista[i].split("|");
				size = +campos[2];
				bytesImagen = blob.slice(x, x + size);
				var blobImagen = new Blob([bytesImagen], { "type": "image/jpg" });
				imagenBlobs.push(blobImagen);
				listaCategorias.push(lista[i]);
				x += size;
			}		
			cArchivos += nRegistros;			
			grupoContador++;
			if((nArchivos<imagenCantidadPagina && grupoContador==grupoTotal) || (cArchivos>=imagenCantidadPagina && soloUnaVez)) {
				mostrarDataConImagenes();
				soloUnaVez = false;
			}
			spnMensaje.innerText = "Cargando: " + cArchivos + " de " + nArchivos;
			pbrConsulta.value++;
			if(grupoContador<grupoTotal){
				await obtenerDataImagenes();
			}
			else {
				txtCodigo.style.display="inline";
				btnBuscar.style.display="inline";
			}
		}
	}
}

function mostrarDataConImagenes(){
	divRpta.innerHTML = "";
	var inicio = imagenContadorPaginas * imagenCantidadPagina;
	var fin = inicio + imagenCantidadPagina;
	var blobImagen;
	var html = "";
	var campos = [];
	for(var i=inicio;i<fin;i++){
		if(i<nArchivos){
			campos = listaCategorias[i].split("|");
			html += "<div class='MarcoImagen2' id='";
			html += campos[0];
			html += "' data-nom='";
			html += campos[1];
			html += "'>";
			blobImagen = imagenBlobs[i];
			html += "<img src='";
			html += URL.createObjectURL(blobImagen);
			html += "' class='Imagen'/>";
			html += "<div>Codigo: ";
			html += campos[0];
			html += "</div>";
			html += "<div>Nombre: ";
			html += campos[1];
			html += "</div>";
			html += "</div>";
		}
		else break;
	}
	divRpta.innerHTML = html;
	txtTotalPaginas.value = imagenTotalPaginas;
	cboPagina.value = imagenContadorPaginas;
	
	programarImagenes();
}

function programarBotones(){
	btnVerCarrito.onclick = function(){
		window.location.href = "Detalles";
	}
	
	btnBuscar.onclick = function(){
		var nRegistros = listaCategorias.length;
		campos = [];
		var codBuscado = txtCodigo.value.toLowerCase();
		var pos = -1;
		for(var i=0;i<nRegistros;i++){
			campos = listaCategorias[i].split("|");
			if(campos[0].toLowerCase()==codBuscado){
				pos = i;
				break;
			}
		}
		if(pos>-1){
			imagenContadorPaginas = Math.floor(pos / imagenCantidadPagina);
			mostrarDataConImagenes();
			var div = document.getElementById(codBuscado);
			if(div!=null) div.className = "MarcoImagen2Sel";
		}
		else alert("No se encontro el Codigo de la Categoria");
	}
	
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
			mostrarDataConImagenes();
		}
	}
}

function programarImagenes(){
	var divs = document.getElementsByClassName("MarcoImagen2");
	var nDivs = divs.length;
	for(var i=0;i<nDivs;i++){
		divs[i].onclick = function(){
			sessionStorage.setItem("IdCategoria", this.id);
			sessionStorage.setItem("NombreCategoria", this.getAttribute("data-nom"));
			window.location.href = "Productos";
		}
	}
}