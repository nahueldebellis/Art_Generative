from p5 import *
def setup():
    background(0)
    size(712, 712, P3D)
    global x
    x = random.uniform(712)
    global y
    y = random.uniform(712)
    
def draw():
    global x, y
    rect_mode(CENTER)
    translate(x.__int__, y.__int__)
    fill(0)
    stroke(255)
    i = random_uniform(0, 360)
    rotate_z(radians(i.__int__%360))
    rect(0, 0, 100,100)
    
    translate(110, 110)
    no_fill()
    stroke(255)
    i = random_uniform(0, 360)
    rotate_z(radians(i.__int__%360))
    rect(0, 0, 100,100)

run()
