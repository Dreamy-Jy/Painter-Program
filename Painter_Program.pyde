"""
by Jordane Thomas,  
"""
from random import *

date =  "{}'{}'{}".format(month(), day(), year()) # format mm/dd/yyyy
saveNum = 0

def setup():
    size(1000,1000)
    background(255,255,255)
"""
considerations
 a continous stream mode caused by pressing C
 
"""
def draw():
    if mousePressed == True:
        fill(randint(0,255),randint(0,255),randint(0,255))
        ellipse(mouseX,mouseY,200,200)

def keyPressed():
    if key == "s":
        saveImg()
        return
    if keyCode == UP:
        print('up')
    if keyCode == DOWN:
        print('down')
# sets an image name based on the date, save number, an a four letter code 
def saveImg():
    time = "{}:{}:{}'milsecs {}".format(hour(),minute(),second(), millis())
    name = 'date; '+ date +', time; '+ time +".png"
    save(name)
    print (name)