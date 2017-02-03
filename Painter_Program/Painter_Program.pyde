"""
by Jordane Thomas,  

Restructure this program for the new Object oriented Style
"""
from random import *
from Paint_tools import *

date =  "{}_{}_{}".format(month(), day(), year()) # format mm/dd/yyyy
lenCirc = 200
widCirc = 200
incrCirc = 5
pointer = PaintTool()

def setup():
    size(1000,600)
    background(255,255,255)
"""
considerations
 a continous stream mode caused by pressing C
 
"""
def draw():
    global lenCirc, widCirc
    background(255)
    fill(randint(0,255),randint(0,255),randint(0,255))
    pointer.draw(mouseX,mouseY)
    

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
        widCirc -= incrCirc

# sets an image name based on the date, save 
def saveImg():
    time = "{}_{}_{}_milsecs {}".format(hour(),minute(),second(), millis())
    name = 'date; '+ date +', time; '+ time +".png"
    save(name)
    print (name)