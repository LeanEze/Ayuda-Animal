const botonimg1 = document.querySelector('.botonimg1')
const boton1 = document.querySelector('.boton1');

boton1.addEventListener('mouseenter', ()=>{
    botonimg1.classList.toggle("activados")
})
boton1.addEventListener('mouseleave',(e)=>{
    botonimg1.classList.remove("activados")
})


