add_library('Mouse2DTransformations')
from random import randint as ri
from processing import *
import mouse

height = 500
width = 500
text_area = 0
old = 0
buttons = [1,2,3,4,5,6,7,8,9,0]
more_than_number = ""



def setup():
    size(width,height)
    frameRate(300)
    fullScreen()
def draw():
    global height
    global width
    fill(255,255,255)
    rect(0,0,width,height) # main background
    
    gui()
    point(100,100)
    
def gui():
    global old
    global more_than_number
    fill(250, 250, 250)
    rect(width-(width-6), height-(height-5), width-10, height-(height-60),7) # text area (adding the pressed numbers to it) 

    fill(250, 250, 250)
    rect(width-(width-6), height-(height-73), width-10, height-75,7) # large box (numbers and sympols)
    
    fill(0,0,0)
    text(more_than_number,width-(width-13),height-(height-50))

    
    fill(250, 250, 250)
    rect(10, 82,100,80)# +
    fill(255,0,0)
    text("+",width-(width-46),height-(height-130))
    
    fill(250, 250, 250)
    rect(10, 182,100,80)# =
    fill(255,0,0)
    text("=",width-(width-46),height-(height-230))
    for index,i in enumerate(buttons):
        if index <= 2: # 1 2 3 button
            fill(250, 250, 250)
            rect(width-(width-160)+(index * 110), height-(height-123), 100,80)
            textSize(28)
            fill(255,0,0)
            text(i,width-(width-200)+(index * 110),height-(height-170))
        elif index <= 5:# 4 5 6  button
            if index == 3:
                old = index
            index = (index - old)
            fill(250, 250, 250)
            rect(width-(width-160)+(index * 110), height-(height-210), 100,80)
            textSize(28)
            fill(255,0,0)
            text(i,width-(width-200)+(index * 110),height-(height-260))
            
        elif index <= 8: # 7 8 9 button
            if index == 6:
                old = index
            index = (index - old)
            fill(250, 250, 250)
            rect(width-(width-160)+(index * 110), height-(height-297), 100,80)
            textSize(28)
            fill(255,0,0)
            text(i,width-(width-200)+(index * 110),height-(height-350))
        elif index <= 9: # 0 button
            if index == 9:
                old = index
            index = (index - old)+1
            fill(250, 250, 250)
            rect(width-(width-160)+(index * 110), height-(height-384), 100,80)
            textSize(28)
            fill(255,0,0)
            text(i,width-(width-200)+(index * 110),height-(height-430))
            
            
def button(x, y,point_x,point_x2,point_y,point_y2):#button function
    '''
    must be    
    point_x < point_x2
    point_y < point_y
    in the same order
    '''
    in_x = point_x <= x <= point_x2
    in_y = point_y <= y <= point_y2
   
    if in_x and in_y:
        return True
    else:
        return False

def clear_function():
    global more_than_number
    more_than_number = ""


def mtn(x):
    global more_than_number
    more_than_number = str(more_than_number)
    more_than_number +=str(x)

def random_color():
    red = ri(1,255)
    green = ri(1,255)
    blue = ri(1,255)
    background(red,green,blue)
    


def processor(x):
    global more_than_number
    total = eval(more_than_number)
    more_than_number = total  
    print(more_than_number)

        


def clicking(x):
    if x == 0:
        if button(mouseX,mouseY,160,260,122,203):#0
            mtn(0)
            print("0 has been added")
    if x == 1:
        if button(mouseX,mouseY,160,260,122,203):#1
            mtn(1)
            print("1 has been added")
    if x == 2:  
        if button(mouseX,mouseY,270,370,122,203):#2
            mtn(2)
            print("2 has been added")
    if x == 3:
        if button(mouseX,mouseY,380,480,122,203):#3
            mtn(3)
            print("3 has been added")
    if x == 4:     
        if button(mouseX,mouseY,160,260,211,290):#4
            mtn(4)
            print("4 has been added")
    if x == 5:  
        if button(mouseX,mouseY,160,260,122,203):#5
            mtn(5)
            print("5 has been added")
    if x == 6:  
        if button(mouseX,mouseY,160,260,122,203):#6
            mtn(6)
            print("6 has been added")
    if x == 7:
        if button(mouseX,mouseY,160,260,122,203):#7
            mtn(7)
            print("7 has been added")
    if x == 8:  
        if button(mouseX,mouseY,160,260,122,203):#8
            mtn(8)
            print("8 has been added")
    if x == 9: 
        if button(mouseX,mouseY,160,260,122,203):#9
            mtn(9)
            print("9 has been added")
        

    
def mouseClicked():
    global more_than_number
    print(mouseX,mouseY)

    if button(mouseX,mouseY,270,370,385,465):#0
        mtn(0)
        print("0 has been added")

    if button(mouseX,mouseY,160,260,122,203):#1
        mtn(1)
        print("1 has been added")
        
    if button(mouseX,mouseY,270,370,122,203):#2
        mtn(2)
        print("2 has been added")
        
    if button(mouseX,mouseY,380,480,122,203):#3
        mtn(3)
        print("3 has been added")
            
    if button(mouseX,mouseY,160,260,211,290):#4
        mtn(4)
        print("4 has been added")
        
    if button(mouseX,mouseY,270,370,211,290):#5
        mtn(5)
        print("5 has been added")
        
    if button(mouseX,mouseY,380,480,211,290):#6
        mtn(6)
        print("6 has been added")

    if button(mouseX,mouseY,160,260,300,376):#7
        mtn(7)
        print("7 has been added")
        
    if button(mouseX,mouseY,270,370,300,376):#8
        mtn(8)
        print("8 has been added")
        
    if button(mouseX,mouseY,380,480,300,376):#9
        mtn(9)
        print("9 has been added")
        
    if button(mouseX,mouseY,10,110,82,161):# +
        mtn("+")
        print("+ has been added")

    if button(mouseX,mouseY,10,110,182,261):# =
        processor(more_than_number)
