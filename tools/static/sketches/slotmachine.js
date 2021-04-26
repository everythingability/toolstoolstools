var data

var img1 , img2, img3
function preload(){
    

}
function setup() {
    createCanvas(900, 500);
    background("yellow")
    textSize(18)
    img1 = loadImage(slot1.image)
    console.log( slot1.image)
    img2 = loadImage(slot2.image)
    console.log( slot2.image)
    img3 = loadImage(slot3.image)
    console.log( slot3.image)

  
  }
  
  function draw() {
    image(img1, 0, 10, 300, 150)
    text(slot1.name, 50, 350, 240, 300)
    text(slot1.image, 50, 400, 240, 300)

    image(img2, 300, 10, 300, 150)
    text(slot2.name, 300, 350, 240, 300)
    text(slot2.image, 300, 420, 240, 300)
    
    image(img3, 600, 10, 300, 150)
    text(slot3.name, 600, 350, 240, 300)
    text(slot3.image, 600, 440, 240, 300)
  }