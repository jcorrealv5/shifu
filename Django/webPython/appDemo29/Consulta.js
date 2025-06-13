window.onload = function(){
	btnConsultar.onclick = async function(){
		var rptaHttp = await fetch("ConsultarProductos?id=" + txtCodigo.value);
		if(rptaHttp.ok){
			var rpta = await rptaHttp.text();
			if(rpta!=""){
				if(!rpta.startsWith("Error")){
					var lista = rpta.split("¬");
					var nRegistros = lista.length;
					if(nRegistros==1){
						lista.splice(0,0,"Codigo|Nombre|IdProv|IdCat|Precio|Stock");
						lista.splice(1,0,"80|300|80|80|80|80");
						lista.splice(2,0,"int|str|int|int|float|int");
					}
					Gui.Grilla(lista, divProducto, "|", null, null, 20, 10, ";", "Producto", false, false, "", false, true, false, null, false, null);
				}
			}
		}
	}
}