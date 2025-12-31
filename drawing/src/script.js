let font;

function preload() {
  font = loadFont('src/QueensidesMedium-x30zV.ttf'); 
}

function setup() {
  createCanvas(400, 400, WEBGL);
  textFont(font);
  textSize(16);
}

function draw() {
  background(200);

  // --- 3D section ---
  rotateY(frameCount * 0.05);
  normalMaterial();
  box(100);

  // --- Switch to 2D overlay ---
  resetMatrix(); // resets the transform to flat 2D
  translate(-width / 2, -height / 2); // move origin to top-left

  // Draw 2D elements
  noStroke();
  fill(0, 100);
  rect(10, 10, 150, 50, 10);

  fill(255);
  textSize(16);
  text("3D Box Example", 20, 40);

    // Draw a black bezier curve.
  noFill();
  stroke(0);
  strokeWeight(5);
  bezier(185, 70, 10, 60, 190, 150, 115, 130);
}
