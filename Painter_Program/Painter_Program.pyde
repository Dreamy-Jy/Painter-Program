"""
by Jordane Thomas,  
weird bug
"""
from random import *

lenCirc = 200
widCirc = 200
incrCirc = 5
pen = Pen();
def setup():
    size(1000,600)
    background(255,255,255)
"""
considerations
 a continous stream mode caused by pressing C
 
"""
def draw():
    pen.draw(mouseX,mouseY)
    """
    noStroke()
    global lenCirc, widCirc
    
    if mousePressed == True:
        fill(randint(0,255),randint(0,255),randint(0,255))
        ellipse( mouseX, mouseY, widCirc, lenCirc)
    """

def keyPressed():
    global incrCirc, lenCirc, widCirc
    if key == "s":
        saveImg()
        return
    if keyCode == UP:
        lenCirc += incrCirc
    if keyCode == DOWN:
        lenCirc -= incrCirc
    if keyCode == RIGHT:
        widCirc += incrCirc
    if keyCode == LEFT:

# sets an image name based on the date, save     
'''
def saveImg():
    date =  "{}_{}_{}".format(month(), day(), year()) # format mm/dd/yyyy
    time = "{}_{}_{}_milsecs {}".format(hour(),minute(),second(), millis())
    name = 'date; '+ date +', time; '+ time +".png"
    save(name)
    print (name)
'''

class Pen(Object):
    """
    Pen follow the mouse and places shapes
    """
    def __init__(self):
        pass
    def draw(self,x,y):
        point(x,y)