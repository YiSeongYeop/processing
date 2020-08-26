change_speed = 0.0005
c = 0

class cell(object):
    def __init__ (self, x, y, c_init):
        self.x = x
        self.y = y
        self.c_init = c_init
        self.w, self.h = 50, 50
        
    def update(self):
        global c
        global change_speed
        change_speed += 0.0005
        c = cos(change_speed+self.c_init)
        
    def display(self):
        global c
        stroke(255)
        fill(abs(c)*255)
        rect(self.x, self.y, self.w, self.h)
        
cell_list = [[cell(50*i, 50*j, 0.18*i+0.5*j) for i in range(10)]for j in range(10)] 

def setup():
    size(1600, 800)
    
def draw():
    background(0)
    for i in range(10):
        for j in range(10):
            cell_list[i][j].update()
            cell_list[i][j].display()
    
    
