class PaintTool(object):
    def __init__(self):
        print("PaintTool Created")
        self.color = [255,255,255]
    
    def draw(self,x,y):
        fill(self.color[0], self.color[1], self.color[2])
        ellipse(x,y, 40,40)

    def paintShape(self, widCirc, lenCirc):
        fill(randint(0,255),randint(0,255),randint(0,255))
        ellipse( mouseX, mouseY, widCirc, lenCirc)
class Shape(object):
    """
    assupmtions about 
    colorVals is an list[0 to 2] that only holds integers that can between 0 and 255. 
    - element [0] is red, [1] green, and [2]blue
    
    *find way to get a universal size and positions for shapes*
    sizeVals is a list[0 to how everymany values that shape needs]
    - element [0] is length, [1] is width
    
    position is a list of []
    """
    def __init__(self, colorVals, sizeVals, position):
        self.colorVals = colorVals
        self.sizeVals = sizeVals
        self.position = position
    def paint():
        pass
class Circle(Shape):
    
    def __init__(self, colorVals, sizeVals, position):
        