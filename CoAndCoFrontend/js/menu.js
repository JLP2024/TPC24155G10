agregarMenu();
function agregarMenu() {
    let nav = document.getElementById("navbar");
    nav.innerHTML =
        `<ul class="navbar-items flexbox-col">
    <li class="navbar-logo flexbox-left">
        <a class="navbar-item-inner flexbox">
            <img class="img-logo" src="./img/Logosf.png" alt=""></img>
        </a>
    </li>
    <li class="navbar-item flexbox-left">
        <a class="navbar-item-inner flexbox-left" href="index.html">
            <div class="navbar-item-inner-icon-wrapper flexbox">
                <img class="ion-icon" src="./img/home.png" alt=""></img>
            </div>
            <span class="link-text">Inicio</span>
        </a>
    </li>
    <li class="navbar-item flexbox-left">
        <a class="navbar-item-inner flexbox-left">
            <div class="navbar-item-inner-icon-wrapper flexbox">
                <img class="ion-icon" src="./img/clothes.png" alt=""></img>
            </div>
            <span class="link-text">Productos</span>
        </a>
        <ul class="navbar-items submenu">
            <li class="navbar-item flexbox-left"><a class="navbar-item-inner flexbox link-texta"
                    href="hombre.html">Hombres</a></li>
            <li class="navbar-item flexbox-left"><a class="navbar-item-inner flexbox link-texta"
                    href="dama.html">Damas</a>
            </li>
            <li class="navbar-item flexbox-left"><a class="navbar-item-inner flexbox link-texta"
                    href="nino.html">Niños</a>
            </li>
        </ul>
    </li>
    <li class="navbar-item flexbox-left">
        <a class="navbar-item-inner flexbox-left" href="contacto.html">
            <div class="navbar-item-inner-icon-wrapper flexbox">
                <img class="ion-icon" src="./img/contacto.png" alt=""></img>
            </div>
            <span class="link-text">Contacto</span>
        </a>
    </li>
    <li class="navbar-item flexbox-left">
        <a class="navbar-item-inner flexbox-left" href="cart.html">
            <div class="navbar-item-inner-icon-wrapper flexbox">
                <img class="ion-icon" src="./img/iconos/carrito.png" alt=""></img>
            </div>
            <span class="link-text" id="cuenta-carrito">0</span>
        </a>
    </li>
    <li class="navbar-item flexbox-left">
        <a class="navbar-item-inner flexbox-left" href="producto.html">
            <div class="navbar-item-inner-icon-wrapper flexbox">
                <img class="ion-icon" src="./img/login1.png" alt=""></img>
            </div>
            <span class="link-text">Admin</span>
        </a>
    </li>
</ul>
`;
}