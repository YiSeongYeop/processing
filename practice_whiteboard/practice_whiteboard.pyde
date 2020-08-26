brushSize = 40
brushColor = 0

def setup():
    size(1600,800)
    background(255)
    
def draw():
    global brushSize, brushColor
    
    if mousePressed:
        stroke(brushColor)
        strokeWeight(brushSize)
        line(pmouseX, pmouseY, mouseX, mouseY)

def keyPressed():
    global brushSize, brushColor
    
    if key == '-':
        brushSize -= 5
    elif key == '=':
        brushSize += 5
    elif key == 'r':
        background(255)
    elif key == ' ':
        brushColor = color(random(255), random(255), random(255))
    elif key == 's':
        save(str(year())+str(month())+str(day())+str(hour())+str(minute())+str(second())+str(millis())+".png")
        print("image saved")
    brushSize = constrain(brushSize, 1, 100)
