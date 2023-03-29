var sources = {
  bg: 'image/bg/kitchen-3.png',
  tile: 'image/tile/wall/1009HL.png'
};

const imageURL = ["image/bg/kitchen-3.png", "image/tile/wall/1009HL.png"]; // list of image URLs
const images = []; /// array to hold images.
var imageCount = 0; // number of loaded images;

// function called once all images have loaded.
function allLoaded() {
  var canvas = document.getElementById("canvas");
  var ctx = canvas.getContext("2d");
  // all images have loaded and can be rendered
  ctx.drawImage(images[1], 0, 0); // draw background
  ctx.drawImage(images[0], 0, 0); // draw foreground
  //ctx.drawImage(bgImg, 0, 0, canvas.width, canvas.height);
}

function loadImages() {
  // iterate each image URL, create, load, and add it to the images array
  imageURL.forEach(src => {  // for each image url
    const image = new Image();
    image.src = src;
    image.onload = () => {
      imageCount += 1;
      if (imageCount === imageURL.length) { // have all loaded????
        allLoaded(); // call function to start rendering
      }
    }
    images.push(image); // add loading image to images array

  });
  // the image onload event will not be called until all current execution is
  // complete.
}
