// ...existing code...
console.log('src/script.js loaded', 'createCanvas type:', typeof createCanvas);

function setup() {
  createCanvas(400, 400, WEBGL);
}
function draw() {
  background(135, 206, 235);
  // Sun
  fill("yellow");
  stroke("orange");
  strokeWeight(5);
  circle(100, -125, 70);

  // Grass
  fill("green");
  stroke("darkgreen");
  strokeWeight(5);
  rect(-200, 100, 400, 200);

 //
  fill("yellow");
  stroke("orange");
  strokeWeight(5);
  orbitControl();
  cone(); 

  // // Tree and bird emojis
  // textSize(250);
  // text("🌳",25,300);
  // textSize(50);
  // text("🕊️",mouseX,mouseY);


}
// ...existing code...