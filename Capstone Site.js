let ellipse_X = 500
function setup(){
  createCanvas(windowWidth, windowHeight)
}

function draw(){
    background(140, 180, 180)

  //rectMode(CENTER)
  fill(125, 220, 255)
  noStroke()
  rect(300, 100, 400, 200)
  triangle(300, 100, 300, 300, 150, 200)
  triangle(700, 100, 700, 300, 850, 200)
  textSize(32)
  fill(0, 0, 0)
  text('Video Game', 400, 175)
  text('Recommendation System', 315, 225)
  fill(125, 220, 255)
  rect(50, 400, 900, 800)
  fill(0, 0, 0)
  textSize(24)
  text('This recommendation algorithm is specifically designed to provide users with a \ncustom tailored list of niche games developed by independent studios. This list is \ngenerated based on the users preferences found through their input games list.', 55, 425)



  //fill(300, 150, 100)
  ellipse(mouseX, mouseY, 50, 50)
  if(mouseX < windowWidth/2){
    fill(100, 150, 300)
  }
  else{
    fill(300, 150, 100)
  }

  print(mouseX)
}
