var myModal = document.getElementById('staticBackdrop');
var modal = bootstrap.Modal.getOrCreateInstance(myModal)
if (sessionStorage.getItem("modalAbierto") === null) {
    modal.show()
    sessionStorage.setItem("modalAbierto", true);
}

