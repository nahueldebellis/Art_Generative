from p5 import *
def setup():
    background(0)
    size(712, 712, P3D)
    
def draw():
    rect_mode(CENTER)
    translate(360, 360)
    fill(0)
    stroke(255)
    i = random_uniform(0, 360)
    rotate_z(radians(i.__int__%360))
    rect(0, 0, 100,100)
    fill(0)
    stroke(255, 0, 0)
    i = random_uniform(0, 360)
    rotate_z(radians(i.__int__%360))
    rect(0, 0, 200,200)
