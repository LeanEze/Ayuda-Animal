const imagenes = document.getElementsByClassName("imagenes");
console.log(imagenes[0].width);
var imagenAncho = imagenes.naturalWidth;
var imagenAlto = imagenes.naturalHeight;
var anchoVentana = window.innerWidth;
var altoVentana = window.innerHeight;
window.addEventListener('load',()=>{

    for (var i = 0; i < imagenes.length; i++) {
        
        var imagen = imagenes[i];
        if (imagen.naturalWidth > imagen.naturalHeight) {
            imagen.style.objectFit = "cover";
        }else{
            imagen.style.objectFit = "contain";
          }
        
      }
})
