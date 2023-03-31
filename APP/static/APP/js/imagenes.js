const imagenes1 = document.querySelector(".imagenes1")
console.log(imagenes1.width)
if(imagenes1.width> imagenes1.height){
    imagenes1.style.objectFit = ""
    console.log("la imagen es mas ancha q alta")

}else{
    console.log("la imagen es mas  alta q ancha ")
}
