from p5 import *
import time

def setup():
    size(1024, 612)

def poli(x, y, puntos, radio):
    angle = 360.0 / puntos
    w = radio / 2.0
    h = radio / 2.0
    s = PShape()
    with s.edit():
        for i in range(puntos.__int__()+1):
            a = x + w * cos(radians(angle*i))
            b = y + h * sin(radians(angle*i))
            s.add_vertex((a, b))
    return s

def draw():
    #s = poli(random_uniform(360), random_uniform(360), random_uniform(5), random_uniform(20))
    #draw_shape(s)
    '''fill(0, 0, 255)
    rect((0, 0), 360, 360)
    fill(255, 0, 0)
    rect((0, 0), 360, 360)'''
    
    fill(random_uniform(60), random_uniform(71, 80), random_uniform(110, 255), 10)
    no_stroke()
    circle((random_uniform(1024), random_uniform(612)), random_uniform(50))   
run(frame_rate = 1000)
