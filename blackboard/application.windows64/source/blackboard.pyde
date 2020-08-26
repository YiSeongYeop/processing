c = color(255, 255, 255)
fixedstrokeweight = 1

def setup():
    global f, pg
    size(1200, 800)
    stroke(255)
    background(0)
    frameRate (1000)
    f = createFont("Arial", 16, True)

def draw():
    global f, c, fixedstrokeweight
    
    fill(255) 
    noStroke()
    rect(10,10,80,50)
    
    fill(0) 
    textFont(f,24)                   
    text("Erase",20,42)
    
    fill(255) 
    noStroke()
    rect(120,10,80,50,5)
    
    fill(0) 
    textFont(f,24)                   
    text("White",130,42)
    
    fill(255,0,0) 
    noStroke()
    rect(230,10,80,50,5)
    
    fill(0) 
    textFont(f,24)                  
    text("Red",246,42)
    
    fill(0,0,255) 
    noStroke()
    rect(340,10,80,50,5)
    
    fill(0) 
    textFont(f,24)                   
    text("Blue",356,42)
    
    fill(0,255,0) 
    noStroke()
    rect(450,10,80,50,5)
    
    fill(0) 
    textFont(f,24)                   
    text("Green",457,42)
    
    fill(255) 
    textFont(f,30)                   
    text("Roll Mouse Wheel to change Thickness",570,46)
    
    strokeWeight(fixedstrokeweight)
    if mousePressed:
        if mouseButton == RIGHT:
            stroke(0)
            smoothline(mouseX, mouseY, pmouseX, pmouseY)
        else:
            stroke(c)
            if mouseX > 10 and mouseX < 90 and mouseY > 10 and mouseY < 60:
                background(0)
            elif mouseX > 120 and mouseX < 200 and mouseY > 10 and mouseY < 60:
                stroke(255,255,255)
                c = color(255, 255, 255)
            elif mouseX > 230 and mouseX < 310 and mouseY > 10 and mouseY < 60:
                stroke(255,0,0)
                c = color(255, 0, 0)
            elif mouseX > 340 and mouseX < 420 and mouseY > 10 and mouseY < 60:
                stroke(0,0,255)
                c = color(0, 0, 255)
            elif mouseX > 450 and mouseX < 530 and mouseY > 10 and mouseY < 60:
                stroke(0,255,0)
                c = color(0, 255, 0)
            else:
                smoothline(mouseX, mouseY, pmouseX, pmouseY)

def smoothline(x, y, px, py):
    global fixedstrokeweight
    speed = float(abs(x-px) + abs(y-py))/10
    strokeWeight(speed+fixedstrokeweight)
    line(mouseX, mouseY, pmouseX, pmouseY)
    
def mouseWheel(event):
    global fixedstrokeweight
    e = float(event.getCount())
    if fixedstrokeweight <= 1:
        fixedstrokeweight += 1
        return 0
    else:
        fixedstrokeweight += e
