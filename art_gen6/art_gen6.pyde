import time
def setup():
    size(1024, 560, P3D)
    
def poligonos(x, y, puntos, radio):
    angulo = 360.0 / puntos
    w = radio / 2.0
    h = radio / 2.0
    beginShape()
    for i in range(puntos.__int__()+1):
        vertex(x * w * cos(angulo * i), y * h * sin(angulo * i))
    endShape()
    
    
def draw():
    background(random(255), random(127), random(127))
    
    for i in range(300): 
        noStroke()   
        fill(random(255), random(255), random(255), 127)
        poligonos(random(360), random(360), random(7), random(10))
    time.sleep(1)
    
