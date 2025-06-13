window.onload = async function(){
	var rptaHttp = await fetch("ListarProductos");
	if(rptaHttp.ok){
		var rpta = await rptaHttp.text();
		var lista = rpta.split("¬");
		Gui.Grilla(lista, divProducto, "|", null, null,20, 10, "¬");
	}
}