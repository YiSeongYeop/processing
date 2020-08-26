distance = 0
click = True

def setup():
    size(1600, 800)
    
def draw():
    global click,distance
    if click == True:
        background(220)
    else:
        background(100)
        
    for i in range(4, height, 20):
        for j in range(4, width, 40):
            distance = dist(j, i , mouseX, mouseY)
            if click:
                fill(255-distance/3, 0, distance/3)
            else:
                fill(random(255), random(255), random(255))
            strokeWeight(3)
            stroke(255-distance/3, 0, distance/3)
            rect(j, i, 32, 12)
            
def mousePressed():
    global click
    if click:
        click = False
    else:
        click = True
