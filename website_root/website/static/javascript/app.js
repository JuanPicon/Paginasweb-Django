
let fechaActual = new Date();
let hora = fechaActual.toLocaleTimeString();
console.log(hora);

let pReloj = document.getElementById("reloj");

function mostrarHora(){
    let fechaActual = new Date();
    pReloj.textContent = fechaActual.toLocaleTimeString();
}
setInterval("mostrarHora()",1000);