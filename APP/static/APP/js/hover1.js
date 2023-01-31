
const boton = document.querySelector('.boton');
const botonimg = document.querySelector('.botonimg')

// ESTA ES LA FUNCION DE EFECTO EN LOS BOTONES DE INICIAR SESION / EDICION Y CERRAR SESION

boton.addEventListener('mouseenter', ()=>{
        botonimg.classList.toggle("activado")


})
boton.addEventListener('mouseleave',(e)=>{
        botonimg.classList.remove("activado")
})





