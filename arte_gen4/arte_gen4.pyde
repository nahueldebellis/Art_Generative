import time
def setup():
    size(1024, 712)
    
def poligonos(x, y, puntos, radio):
    angulo = TWO_PI / puntos
    w = radio * 2.0
    h = radio * 2.0
    beginShape()
    for i in range(puntos.__int__()+1):
        vertex(x + w * cos(angulo * i), y + h * sin(angulo * i))
    endShape()
    
    
def draw():
    r = random(1024)
    y = random(712)
    translate(mouseX, mouseY)
    fill(random(255), random(255), random(255), 127)
    noStroke()
    poligonos(0, 0, random(7), random(50))
    time.sleep(0.05)
    