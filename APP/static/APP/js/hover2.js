const boton2 = document.querySelector('.boton2');
const botonimg2 = document.querySelector('.botonimg2')


boton2.addEventListener('mouseenter', ()=>{
    botonimg2.classList.toggle("activados")
})
boton2.addEventListener('mouseleave',(e)=>{
    botonimg2.classList.remove("activados")
})

