
var img
var font

function preload(){
    font = loadFont("/static/fonts/Franklin Gothic Heavy Italic.ttf")
    console.log(image_url)
    //img = loadImage(image_url)
}

function setup() {
    createCanvas(800, 400);
    background("red")
    textFont(font)
    console.log("img_url:", image_url)
   
    
    

  }
  
  function draw() {
    background("red")
    fill("white")
   //image(img, 0, 0)
   text(name, 20, 20)
  }