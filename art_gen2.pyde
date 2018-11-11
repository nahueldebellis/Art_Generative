def setup():
    background(0)
    size(712, 712, P3D)
    
def draw():
    rectMode(CENTER)
    translate(360, 360)
    fill(0)
    stroke(255)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 100,100)
    fill(0)
    stroke(255, 0, 0)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 200,200)
