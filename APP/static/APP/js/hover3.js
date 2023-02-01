const botonimg1 = document.querySelector('.botonimg1')
const boton1 = document.querySelector('.boton1');

// ESTA ES LA FUNCION DE EFECTO EN LOS BOTONES DE INICIAR SESION / EDICION Y CERRAR SESION
boton1.addEventListener('mouseenter', ()=>{
    botonimg1.classList.toggle("activados")
})
boton1.addEventListener('mouseleave',(e)=>{
    botonimg1.classList.remove("activados")
})


