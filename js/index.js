const contenedorTarjetas = document.getElementById("productos-container");

/** Crea las tarjetas de productos teniendo en cuenta la lista en dama.js */
function crearTarjetasProductosInicio(productos){
  productos.forEach(producto => {
    const nuevaDama = document.createElement("div");
    nuevaDama.classList = "tarjeta-producto"
    nuevaDama.innerHTML = `
    <img src="./img/productos/${producto.id}.jpg" alt="Dama1">
    <h3>${producto.nombre}</h3>
    <p class="precio">$${producto.precio}</p>
    <button>Agregar al carrito</button>`
    contenedorTarjetas.appendChild(nuevaDama);
    nuevaDama.getElementsByTagName("button")[0].addEventListener("click",() => agregarAlCarrito(producto))
  });
}
crearTarjetasProductosInicio(dama);