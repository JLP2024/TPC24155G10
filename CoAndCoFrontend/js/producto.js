const url = "https://jelp.pythonanywhere.com/"
//const url = "http://127.0.0.1:5000/"

const contenedor =document.querySelector('tbody')
let opcion =""
let imagenSeleccionada
let imagensql=""

let modalProducto = new bootstrap.Modal(document.getElementById('modalProducto'))
const formProducto = document.getElementById('form-modal')//querySelector('form')
const btnAgregar = document.getElementById('btn-agregar')
const titulo = document.getElementById('modalLabel')
const imagenVistaPrevia = document.getElementById('imagen-vista-previa');

const obtenerDatos = () => {
    const datos = new FormData(formProducto);
    const datosProducto = Object.fromEntries(datos.entries());
    for(var pair of datos.entries()) {
        console.log(pair[0]+ ', '+ pair[1]);
    }
    formProducto.reset();
    return datos;
}

const obtenerDatosEdicion = () => {
    const datos = new FormData(formProducto);
    if (imagenSeleccionada) {
        datos.set('imagen', imagenSeleccionada, imagenSeleccionada.name);
    }else{
        datos.set('imagen', imagensql)
    }
    for(var pair of datos.entries()) {
        console.log(pair[0]+ ', '+ pair[1]);
    }
    formProducto.reset();
    return datos;
}

const listarProductos = async () => {
    try {
        const response = await fetch(url + 'productos/listar');
        const productos = await response.json();
        let contenido = ``;
        productos.forEach((producto, index) => {
            sexo=""
            switch (producto.genero) {
                case 1:
                    sexo = "CABALLERO"
                    break
                case 2:
                    sexo = "DAMA"
                    break
                case 3:
                    sexo = "NIÑOS"
                    break
                case 4:
                    sexo = "UNISEX"
                    break
                default:
                    console.log("El resultado no existe")
            }
            ima = '<img src=https://www.pythonanywhere.com/user/jelp/files/home/jelp/apicoyco/static/imagenes/' + producto.imagen +' alt="Imagen del producto" style="width: 80px;"></img>'
            //ima  = '<img src = ../../CoAndCoApi/static/imagenes/' +  producto.imagen + ' alt="Imagen del producto" style="width: 80px"></img>'
            contenido += `
                <tr class="text-center form-control-sm">
                    <td>${producto.id}</td>
                    <td>${producto.codigoProducto}</td>
                    <td>${producto.nombre}</td>
                    <td>${sexo}</td>
                    <td>${producto.talle}</td>
                    <td>${producto.color}</td>
                    <td>${producto.precio}</td>
                    <td>${producto.stock}</td>
                    <td>
                        ${ima}
                    </td>
                    <td>
                        <button class="btnEditar  btn-sm  btn btn-outline-primary">Editar</button>
                        <button class="btnBorrar btn btn-sm  btn btn-outline-danger">Eliminar</button>
                    </td>
                </tr>`;
        });
        contenedor.innerHTML = contenido;
    } catch (ex) {
        alert(ex);
    }
};

const on = (element, event, selector, handler)=>{
    element.addEventListener(event,e =>{
        if(e.target.closest(selector)){
            handler(e)
        }
    })
}

on(document,'click', '.btnBorrar',e=>{
    const fila = e.target.parentNode.parentNode
    const id = fila.firstElementChild.innerHTML
    alertify.confirm("Esta seguro de eliminar?",
    function(){
        borrarProducto(id);
        alertify.success('Ok');
    },
    function(){
        alertify.error('Cancel');
    });
})

const borrarProducto = async(id) =>{
    try{
        const response = await fetch(url + 'productos/borrar/' + id,{
        method:'DELETE',
        headers:{'Content-Type': 'application/json'}
    });
    }catch(error){
        console.log(error)
    }
    listarProductos()
}

const buscarProducto = async(id)=>{
    try{
        console.log(id)
        const response = await fetch(url + 'productos/listar/' + id);
        const producto = await response.json();
        console.log(producto.codigoProducto)
        codigoProducto.value = producto.codigoProducto
        nombre.value = producto.nombre
        genero.value = producto.genero
        talle.value = producto.talle
        color.value = producto.color
        precio.value = producto.precio
        stock.value = producto.stock
        imagen = producto.imagen
        imagensql = producto.imagen;
        console.log('segundo')
        imagenVistaPrevia.src = ""
        opcion = "editar"
        modalProducto.show()
        }catch(error){
        console.log(error)
    }
}

let idform = 0
on(document,'click', '.btnEditar', e => {
    const fila = e.target.parentNode.parentNode
    idform = fila.children[0].innerHTML
    buscarProducto(idform)
}),

formProducto.addEventListener('submit', (e) =>{
    e.preventDefault()
    if(opcion=='agregar'){
        crearProducto()
    }
    if(opcion=='editar'){
        console.log('antes1')
        editarProducto(idform)
    }
})

const crearProducto = async() =>{
    const datos = obtenerDatos()
    try {
        const response = await fetch(url + 'productos/agregar',{
            method:'POST',
            body:datos  
        });
        if(response.ok){
            listarProductos()
        }
        modalProducto.hide()
    } catch (error) {
        console.log(error);
    }
};

function seleccionarImagen(event) {
    const file = event.target.files[0];
    imagenSeleccionada = file;
    console.log(imagenSeleccionada)
    imagenUrlTemp = URL.createObjectURL(file); // Crea una URL temporal para la vista previa
    imagenVistaPrevia.src = imagenUrlTemp;
    imagenVistaPrevia.style.display = 'inline';
}

const editarProducto = async(id) =>{
    const datos = obtenerDatosEdicion()
    try {
        const response = await fetch(url + 'productos/' + id,{
            method:'PUT',
            body:datos
        });
        if(response.ok){
            modalProducto.hide()
            listarProductos()
        }
    } catch (error) {
        console.log(error);
    }
};

window.addEventListener("load", async () => {
    await listarProductos();
});

btnAgregar.addEventListener('click', () => {
    codigoProducto.value =''
    nombre.value = ''
    genero.value =''
    talle.value = ''
    color.value = ''
    precio.value =''
    stock.value = ''
    modalProducto.show()
    opcion = "agregar"
})

document.getElementById('imagen').addEventListener('change', seleccionarImagen);
