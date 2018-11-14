def setup():
    background(0)
    size(712, 712, P3D)
    global x
    x = random(712)
    global y 
    y = random(712)
    
def draw():

    rectMode(CENTER)
    translate(width/2, height/2)
    fill(0)
    stroke(255)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 100,100)    
    pushMatrix()
    translate(175, 175)
    noFill()
    stroke(255)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 100,100)
    popMatrix()
    translate(300, 300)
    fill(random(255), random(255), random(255), 127)
    stroke(255)
    i = random(0, 360)
    rotateZ(radians(i%360))
    rect(0, 0, 100, 100)
