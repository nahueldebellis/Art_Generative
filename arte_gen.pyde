def setup():
    background(0)
    size(712, 712, P3D)
    global x
    x = random(712)
    global y 
    y = random(712)
def draw():
    rectMode(CENTER)
    translate(x, y)
    fill(0)
    stroke(255)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 100,100)
    
    translate(175, 175)
    noFill()
    stroke(255)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 100,100)
