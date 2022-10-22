const perro3 = document.querySelector('.perro3');
const perro2 = document.querySelector('.perro2');
const perro = document.querySelector('.perro');
const vacio = document.querySelector('.vacio');



perro3.addEventListener('click',()=>{
    vacio.innerHTML=`<img src="/static/APP/css/perro3.jpg" alt="" class="d-block w-100 imagenes">`;

})



perro.addEventListener('click',()=>{
    vacio.innerHTML=`<img src="/static/APP/css/perro.jpg" alt="" class="d-block w-100 imagenes">`;

})



perro2.addEventListener('click',()=>{
    vacio.innerHTML=`<img  src="/static/APP/css/perro2.jpg" alt="" class="d-block w-100 imagenes">`;

})