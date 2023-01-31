const centrado = document.querySelector('.loader')
const elbody = document.querySelector("body")
const dog = document.querySelector('.dog')
const hiddenbar = document.querySelector('.hiddenbar')

// 
window.addEventListener('load',()=>{
    elbody.classList.remove('hidden')
    centrado.style.display = "none"
})