
const boton = document.querySelector('.boton');
const botonimg = document.querySelector('.botonimg')



boton.addEventListener('mouseenter', ()=>{
        botonimg.classList.toggle("activado")


})
boton.addEventListener('mouseleave',(e)=>{
        botonimg.classList.remove("activado")
})





