sizing = 400
Yplace = 400

def setup():
    global f
    size(1200, 800)
    #background(126)
    #noStroke()
    f = createFont("Arial",16,True)

def draw():
    global sizing, f, Yplace
    background(126)
    sizeofmoon = str(sizing)
    fill(255)
    textFont(f,36)
    text("moon size : "+sizeofmoon,10,40)
    
    Ys = str(Yplace)
    fill(255)
    textFont(f,36)
    text("moon Y place : "+Ys,10,80)
    
    fill(255)
    textFont(f,36)
    text("Roll Mouse Wheel to change Size",10,120)
    
    fill(255)
    textFont(f,36)
    text("size of sun is 400",450,40)
    
    fill(255) 
    noStroke()
    rect(900,10,80,50)
    
    fill(0) 
    textFont(f,24)                   
    text("Y up",915,42)
    
    fill(255) 
    noStroke()
    rect(1010,10,80,50)
    
    fill(0) 
    textFont(f,24)                   
    text("Y down",1011,42)
    
    fill(237,169,0)
    stroke(237,169,0)
    ellipse(600, 400, 400, 400)   # Top circle
    fill(10)
    stroke(10)
    
    if mousePressed and mouseButton == LEFT:
        if mouseX > 900 and mouseX < 980 and mouseY > 10 and mouseY < 60:
            Yplace -= 1
        elif mouseX > 1010 and mouseX < 1090 and mouseY > 10 and mouseY < 60:
            Yplace += 1
    ellipse(mouseX, Yplace, sizing, sizing)   # Middle circle
    
def mouseWheel(event): 
    global sizing
    e = event.getCount()
    sizing += event.getCount()
    
