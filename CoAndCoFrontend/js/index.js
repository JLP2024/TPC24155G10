const contenedorTarjetas = document.getElementById("productos-container");

function getNameURLWeb() {
  var sPath = window.location.pathname;
  var sPage = sPath.substring(sPath.lastIndexOf('/') + 1);
  return sPage;
}
var nombreweb = getNameURLWeb();


/** Crea las tarjetas de productos teniendo en cuenta la lista en .js */
function crearTarjetasProductosInicio(productos, genero) {
  productos.forEach(producto => {
    const nuevaTarjeta = document.createElement("div");
    nuevaTarjeta.classList = "tarjeta-producto"
    nuevaTarjeta.innerHTML = `
    <img src="./img/productos/${producto.id}.jpg" alt="Dama1">
    <h3>${producto.nombre}</h3>
    <p class="precio">$${producto.precio}</p>
    <button>Agregar al carrito</button>`
    contenedorTarjetas.appendChild(nuevaTarjeta);
    nuevaTarjeta.getElementsByTagName("button")[0].addEventListener("click", () => agregarAlCarrito(producto))
  });
}


/** seteo de donde leer de acuerdo a la pag donde esta */
if (nombreweb === "dama.html") {
  proventa = dama;
  var genero= "dama"
}else{
  if (nombreweb === "hombre.html") {
    proventa = hombre
    var genero = "hombre"  
  }else{
   proventa = nino
   var genero = "nino"  
  }
}
crearTarjetasProductosInicio(proventa, genero);








