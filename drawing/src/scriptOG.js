// ...existing code...
console.log('src/script.js loaded', 'createCanvas type:', typeof createCanvas);

function setup() {
  createCanvas(400, 400);
}
function draw() {
  background(135, 206, 235);
  // Sun
  fill("yellow");
  stroke("orange");
  strokeWeight(5);
  circle(300, 50, 70);

  // Grass
  fill("green");
  stroke("darkgreen");
  strokeWeight(5);
  rect(0, 300, 400, 400);

  // Tree and bird emojis
  textSize(250);
  text("🌳",25,300);
  textSize(50);
  text("🕊️",mouseX,mouseY);


}
// ...existing code...