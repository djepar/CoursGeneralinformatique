
const myImages = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"];
(function(){
    "use strict";
    var currentImages = 0;
    //document.getElementById("next").onclick = NextPhoto; 
    const nextPhoto = document.getElementById("next");
    nextPhoto.addEventListener("click", function (){
        currentImages++;
        if (currentImages > myImages.length - 1){
            currentImages = 0;
        }
       
        document.getElementById("myimage").src = myImages[currentImages];
    })
    const previousPhoto = document.getElementById("previous");
    //document.getElementById("previous").onclick = NextPhoto; 
    previousPhoto.addEventListener("click", function (){
        currentImages--;
        if (currentImages < 0){
            currentImages = myImages.length - 1;
        }
       
        document.getElementById("myimage").src = myImages[currentImages];
    })

}) ()