change_speed = 0.01

class cell(object):
    def __init__ (self, x, y, c_init):
        self.x = x
        self.y = y
        self.c_init = c_init
        self.w, self.h = 50, 50
        
    def display(self):
        stroke(255)
        fill(abs(c)*255)
        rect(self.x, self.y, self.w, self.h)
        
    def update(self):
        global c
        global change_speed
        change_speed += 0.01
        c = cos(change_speed+self.c_init)
            
cell_list = [cell(50*i, 0, 0.18*i) for i in range(10)]

def setup():
    size(1600, 800)
    
def draw():
    background(0)
    for i in range(10):
        cell_list[i].update()
        cell_list[i].display()
    
    
