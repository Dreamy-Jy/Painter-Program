class PaintTool(object):
    def __init__(self):
        print("PaintTool Created")
    
    def draw(self,x,y):
        point(x,y)
    
    def paintShape(self, widCirc, lenCirc):
        fill(randint(0,255),randint(0,255),randint(0,255))
        ellipse( mouseX, mouseY, widCirc, lenCirc)