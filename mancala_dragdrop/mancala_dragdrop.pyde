class marble:
    def __init__ (self, x, y, r1, r2):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
        self.st = False
    
    def checkClicked(self, cx, cy):
        if dist(mouseX, mouseY, self.x, self.y) < self.r1:
            self.st = True
        else:
            self.st = False
    
    def update(self):
        if self.st:
            self.x += mouseX - pmouseX
            self.y += mouseY - pmouseY
                
    def display(self):
        fill(250)
        stroke(0)
        strokeWeight(1)
        ellipse(self.x, self.y, self.r1, self.r2)
        
#must make class array ex>boxes = box[numbers]
#and we can give init by for loop
# for i in range(number)
    #boxes[i].update() like this
    
mar1_1 = marble(250, 60, 50, 50)
mar1_2 = marble(340, 60, 50, 50)
mar1_3 = marble(250, 120, 50, 50)
mar1_4 = marble(340, 120, 50, 50)

mar2_1 = marble(450, 60, 50, 50)
mar2_2 = marble(540, 60, 50, 50)
mar2_3 = marble(450, 120, 50, 50)
mar2_4 = marble(540, 120, 50, 50)

mar3_1 = marble(650, 60, 50, 50)
mar3_2 = marble(740, 60, 50, 50)
mar3_3 = marble(650, 120, 50, 50)
mar3_4 = marble(740, 120, 50, 50)

mar4_1 = marble(850, 60, 50, 50)
mar4_2 = marble(940, 60, 50, 50)
mar4_3 = marble(850, 120, 50, 50)
mar4_4 = marble(940, 120, 50, 50)

mar5_1 = marble(1050, 60, 50, 50)
mar5_2 = marble(1140, 60, 50, 50)
mar5_3 = marble(1050, 120, 50, 50)
mar5_4 = marble(1140, 120, 50, 50)

mar6_1 = marble(1250, 60, 50, 50)
mar6_2 = marble(1340, 60, 50, 50)
mar6_3 = marble(1250, 120, 50, 50)
mar6_4 = marble(1340, 120, 50, 50)

mar7_1 = marble(250, 460, 50, 50)
mar7_2 = marble(340, 460, 50, 50)
mar7_3 = marble(250, 520, 50, 50)
mar7_4 = marble(340, 520, 50, 50)

mar8_1 = marble(450, 460, 50, 50)
mar8_2 = marble(540, 460, 50, 50)
mar8_3 = marble(450, 520, 50, 50)
mar8_4 = marble(540, 520, 50, 50)

mar9_1 = marble(650, 460, 50, 50)
mar9_2 = marble(740, 460, 50, 50)
mar9_3 = marble(650, 520, 50, 50)
mar9_4 = marble(740, 520, 50, 50)

mar10_1 = marble(850, 460, 50, 50)
mar10_2 = marble(940, 460, 50, 50)
mar10_3 = marble(850, 520, 50, 50)
mar10_4 = marble(940, 520, 50, 50)

mar11_1 = marble(1050, 460, 50, 50)
mar11_2 = marble(1140, 460, 50, 50)
mar11_3 = marble(1050, 520, 50, 50)
mar11_4 = marble(1140, 520, 50, 50)

mar12_1 = marble(1250, 460, 50, 50)
mar12_2 = marble(1340, 460, 50, 50)
mar12_3 = marble(1250, 520, 50, 50)
mar12_4 = marble(1340, 520, 50, 50)

def setup ():
    size (1600,800)
    background(189,132,57)
    noStroke()
    
def gameboard ():
    background(189,132,57)
    fill (140,83,27)
    rect (25,25,150,750)
    rect (1425,25,150,750)
    
    rect (210,25,180,350)
    rect (410,25,180,350)
    rect (610,25,180,350)
    rect (810,25,180,350)
    rect (1010,25,180,350)
    rect (1210,25,180,350)
    
    rect (210,425,180,350)
    rect (410,425,180,350)
    rect (610,425,180,350)
    rect (810,425,180,350)
    rect (1010,425,180,350)
    rect (1210,425,180,350)
    
    fill (114,77,51)
    rect (165,25,10,750)
    rect (25,765,150,10)
    rect (1565,25,10,750)
    rect (1425,765,150,10)
    
    rect (380,25,10,350)
    rect (210,365,180,10)
    rect (580,25,10,350)
    rect (410,365,180,10)
    rect (780,25,10,350)
    rect (610,365,180,10)
    rect (980,25,10,350)
    rect (810,365,180,10)
    rect (1180,25,10,350)
    rect (1010,365,180,10)
    rect (1380,25,10,350)
    rect (1210,365,180,10)
    
    rect (380,425,10,350)
    rect (210,765,180,10)
    rect (580,425,10,350)
    rect (410,765,180,10)
    rect (780,425,10,350)
    rect (610,765,180,10)
    rect (980,425,10,350)
    rect (810,765,180,10)
    rect (1180,425,10,350)
    rect (1010,765,180,10)
    rect (1380,425,10,350)
    rect (1210,765,180,10)
    #game board finish

def draw ():
    global mar1_1, mar1_2, mar1_3, mar1_4
    global mar2_1, mar2_2, mar2_3, mar2_4
    global mar3_1, mar3_2, mar3_3, mar3_4
    global mar4_1, mar4_2, mar4_3, mar4_4
    
    global mar5_1, mar5_2, mar5_3, mar5_4
    global mar6_1, mar6_2, mar6_3, mar6_4
    global mar7_1, mar7_2, mar7_3, mar7_4
    global mar8_1, mar8_2, mar8_3, mar8_4
    
    global mar9_1, mar9_2, mar9_3, mar9_4
    global mar10_1, mar10_2, mar10_3, mar10_4
    global mar11_1, mar11_2, mar11_3, mar11_4
    global mar12_1, mar12_2, mar12_3, mar12_4
    gameboard()
    
    mar1_1.display()
    mar1_2.display()
    mar1_3.display()
    mar1_4.display()
    
    mar2_1.display()
    mar2_2.display()
    mar2_3.display()
    mar2_4.display()
    
    mar3_1.display()
    mar3_2.display()
    mar3_3.display()
    mar3_4.display()
    
    mar4_1.display()
    mar4_2.display()
    mar4_3.display()
    mar4_4.display()
    
    mar5_1.display()
    mar5_2.display()
    mar5_3.display()
    mar5_4.display()
    
    mar6_1.display()
    mar6_2.display()
    mar6_3.display()
    mar6_4.display()
    
    mar7_1.display()
    mar7_2.display()
    mar7_3.display()
    mar7_4.display()
    
    mar8_1.display()
    mar8_2.display()
    mar8_3.display()
    mar8_4.display()
    
    mar9_1.display()
    mar9_2.display()
    mar9_3.display()
    mar9_4.display()
    
    mar10_1.display()
    mar10_2.display()
    mar10_3.display()
    mar10_4.display()
    
    mar11_1.display()
    mar11_2.display()
    mar11_3.display()
    mar11_4.display()
    
    mar12_1.display()
    mar12_2.display()
    mar12_3.display()
    mar12_4.display()
    
def mousePressed():
    mar1_1.checkClicked(mouseX,mouseY)
    mar1_2.checkClicked(mouseX,mouseY)
    mar1_3.checkClicked(mouseX,mouseY)
    mar1_4.checkClicked(mouseX,mouseY)
    
    mar2_1.checkClicked(mouseX,mouseY)
    mar2_2.checkClicked(mouseX,mouseY)
    mar2_3.checkClicked(mouseX,mouseY)
    mar2_4.checkClicked(mouseX,mouseY)
    
    mar3_1.checkClicked(mouseX,mouseY)
    mar3_2.checkClicked(mouseX,mouseY)
    mar3_3.checkClicked(mouseX,mouseY)
    mar3_4.checkClicked(mouseX,mouseY)
    
    mar4_1.checkClicked(mouseX,mouseY)
    mar4_2.checkClicked(mouseX,mouseY)
    mar4_3.checkClicked(mouseX,mouseY)
    mar4_4.checkClicked(mouseX,mouseY)
    
    mar5_1.checkClicked(mouseX,mouseY)
    mar5_2.checkClicked(mouseX,mouseY)
    mar5_3.checkClicked(mouseX,mouseY)
    mar5_4.checkClicked(mouseX,mouseY)
    
    mar6_1.checkClicked(mouseX,mouseY)
    mar6_2.checkClicked(mouseX,mouseY)
    mar6_3.checkClicked(mouseX,mouseY)
    mar6_4.checkClicked(mouseX,mouseY)
    
    mar7_1.checkClicked(mouseX,mouseY)
    mar7_2.checkClicked(mouseX,mouseY)
    mar7_3.checkClicked(mouseX,mouseY)
    mar7_4.checkClicked(mouseX,mouseY)
    
    mar8_1.checkClicked(mouseX,mouseY)
    mar8_2.checkClicked(mouseX,mouseY)
    mar8_3.checkClicked(mouseX,mouseY)
    mar8_4.checkClicked(mouseX,mouseY)
    
    mar9_1.checkClicked(mouseX,mouseY)
    mar9_2.checkClicked(mouseX,mouseY)
    mar9_3.checkClicked(mouseX,mouseY)
    mar9_4.checkClicked(mouseX,mouseY)
    
    mar10_1.checkClicked(mouseX,mouseY)
    mar10_2.checkClicked(mouseX,mouseY)
    mar10_3.checkClicked(mouseX,mouseY)
    mar10_4.checkClicked(mouseX,mouseY)
    
    mar11_1.checkClicked(mouseX,mouseY)
    mar11_2.checkClicked(mouseX,mouseY)
    mar11_3.checkClicked(mouseX,mouseY)
    mar11_4.checkClicked(mouseX,mouseY)
    
    mar12_1.checkClicked(mouseX,mouseY)
    mar12_2.checkClicked(mouseX,mouseY)
    mar12_3.checkClicked(mouseX,mouseY)
    mar12_4.checkClicked(mouseX,mouseY)
    
def mouseDragged():
    mar1_1.update()
    mar1_2.update()
    mar1_3.update()
    mar1_4.update()
    
    mar2_1.update()
    mar2_2.update()
    mar2_3.update()
    mar2_4.update()
    
    mar3_1.update()
    mar3_2.update()
    mar3_3.update()
    mar3_4.update()
    
    mar4_1.update()
    mar4_2.update()
    mar4_3.update()
    mar4_4.update()

    mar5_1.update()
    mar5_2.update()
    mar5_3.update()
    mar5_4.update()
    
    mar6_1.update()
    mar6_2.update()
    mar6_3.update()
    mar6_4.update()
    
    mar7_1.update()
    mar7_2.update()
    mar7_3.update()
    mar7_4.update()
    
    mar8_1.update()
    mar8_2.update()
    mar8_3.update()
    mar8_4.update()
    
    mar9_1.update()
    mar9_2.update()
    mar9_3.update()
    mar9_4.update()
    
    mar10_1.update()
    mar10_2.update()
    mar10_3.update()
    mar10_4.update()
    
    mar11_1.update()
    mar11_2.update()
    mar11_3.update()
    mar11_4.update()
    
    mar12_1.update()
    mar12_2.update()
    mar12_3.update()
    mar12_4.update()
    
def mouseReleased():
    mar1_1.clicked = False
    mar1_2.clicked = False
    mar1_3.clicked = False
    mar1_4.clicked = False
    
    mar2_1.clicked = False
    mar2_2.clicked = False
    mar2_3.clicked = False
    mar2_4.clicked = False
    
    mar3_1.clicked = False
    mar3_2.clicked = False
    mar3_3.clicked = False
    mar3_4.clicked = False
    
    mar4_1.clicked = False
    mar4_2.clicked = False
    mar4_3.clicked = False
    mar4_4.clicked = False
    
    mar5_1.clicked = False
    mar5_2.clicked = False
    mar5_3.clicked = False
    mar5_4.clicked = False
    
    mar6_1.clicked = False
    mar6_2.clicked = False
    mar6_3.clicked = False
    mar6_4.clicked = False
    
    mar7_1.clicked = False
    mar7_2.clicked = False
    mar7_3.clicked = False
    mar7_4.clicked = False
    
    mar8_1.clicked = False
    mar8_2.clicked = False
    mar8_3.clicked = False
    mar8_4.clicked = False
    
    mar9_1.clicked = False
    mar9_2.clicked = False
    mar9_3.clicked = False
    mar9_4.clicked = False
    
    mar10_1.clicked = False
    mar10_2.clicked = False
    mar10_3.clicked = False
    mar10_4.clicked = False
    
    mar11_1.clicked = False
    mar11_2.clicked = False
    mar11_3.clicked = False
    mar11_4.clicked = False
    
    mar12_1.clicked = False
    mar12_2.clicked = False
    mar12_3.clicked = False
    mar12_4.clicked = False
