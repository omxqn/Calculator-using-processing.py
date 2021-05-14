add_library('Mouse2DTransformations')
import re
from random import randint as ri
from processing import *
import mouse

height = 500
width = 500
text_area = 0
old = 0
buttons = [1,2,3,4,5,6,7,8,9,0]
more_than_number = ""
fp = 0
r = 0
inputs = True
sy_inputs = True
def setup():
    size(width,height)
    frameRate(300)
    #fullScreen()
def draw():
    global height
    global width
    global r
    global frameCount
    r+=60
    fill(255,255,255)
    rect(0,0,width,height) # main background

    gui()
    

    
    
def gui():
    global old
    global more_than_number

    
    
    
    
    fill(250, 250, 250)
    rect(width-(width-6), height-(height-5), width-10, height-(height-60),7) # text area (adding the pressed numbers to it) 

    fill(250, 250, 250)
    rect(width-(width-6), height-(height-73), width-10, height-75,7) # large box (numbers and sympols)
    
    fill(0,0,0)
    text(more_than_number,width-(width-13),height-(height-50))
    
    
    buttons_text() # buttons text
    
    
    
    
    fill(250, 250, 250)
    rect(10, 78,100,80)# +
    fill(255,0,0)
    text("+",width-(width-46),height-(height-130))
    
    fill(250, 250, 250)
    rect(10, 165,100,80)# -
    fill(255,0,0)
    text("-",width-(width-46),height-(height-217))
    
    
    fill(250, 250, 250)
    rect(10, 252,100,80)# *
    fill(255,0,0)
    text("*",width-(width-46),height-(height-304))
    
    
    fill(250, 250, 250)
    rect(10, 339,100,80)# /
    fill(255,0,0)
    text("/",width-(width-46),height-(height-391))  
    
    
    fill(250, 250, 250)
    rect(10, 426,100,70)# =
    fill(255,0,0)
    text("=",width-(width-46),height-(height-478))  
    
    
    
    
    fill(250, 250, 250)
    rect(139, 426,100,70)# =
    fill(255,0,0)
    text("Clear",width-(width-150),height-(height-478))  
    


            
            
    textSize(23)
            
    fill(0,0,255)
    text("MADE BY AZZAM",286,489)
            
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




def buttons_text():
    
    
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
            

def clear_function():
    global more_than_number
    global sy_inputs
    global inputs
    
    inputs = True
    sy_inputs = True
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
    global inputs
    global sy_inputs
    try:
        
        
        
        split_string = re.split("([()*/+-])", more_than_number)
        print(split_string)

        final_string = ""
        for element in split_string:
            if element.isdigit():
                final_string += "float({0})".format(element)
            else:
                final_string += element
        
    
        total = eval(final_string)
        more_than_number = total  
        print(more_than_number)
        inputs = False
        sy_inputs = True
    except:
        print("Invalid input")
        more_than_number = more_than_number
        inputs = True
        


def clicking(x):
    '''
    Adding the numbers when keyboard pressed
    '''
    global inputs
    global sy_inputs
    try:
        x = int(x)
        if x == 0 and inputs:
        
            mtn(0)
            print("0 has been added")
        elif x == 1 and inputs:
    
            mtn(1)
            print("1 has been added")
        elif x == 2 and inputs:  
    
            mtn(2)
            print("2 has been added")
        elif x == 3 and inputs:
        
            mtn(3)
            print("3 has been added")
        elif x == 4 and inputs:     
        
            mtn(4)
            print("4 has been added")
        elif x == 5 and inputs:  
    
            mtn(5)
            print("5 has been added")
        elif x == 6 and inputs:  
        
            mtn(6)
            print("6 has been added")
        elif x == 7 and inputs:
    
            mtn(7)
            print("7 has been added")
        elif x == 8 and inputs:  
    
            mtn(8)
            print("8 has been added")
        elif x == 9 and inputs: 
    
            mtn(9)
            print("9 has been added")
            
        print(x)
    except:
        x = str(x)
        
        if x == "+" and sy_inputs and  more_than_number != "" :# +
            mtn("+")
            print("+ has been added")
            inputs = True
            sy_inputs = False
    
    
    
        elif x == "-" and sy_inputs and  more_than_number != "" :# -
            mtn("-")
            print("- has been added")
            
            inputs = True
            sy_inputs = False
        elif x == "+" and sy_inputs and  more_than_number != "" :# *
            mtn("*")
            print("* has been added")
            inputs = True
            sy_inputs = False
            
    
        elif x == "/" and sy_inputs and  more_than_number != "" :# /
            mtn("/")
            print("/ has been added")
            inputs = True
            sy_inputs = False
            
        elif x == "=":# =
            processor(more_than_number)
            print(x)
        
def mouseClicked():
    global more_than_number
    global inputs
    global sy_inputs
    print(mouseX,mouseY)
    print(inputs)
    if button(mouseX,mouseY,270,370,385,465) and inputs:#0
        mtn(0)
        print("0 has been added")

    if button(mouseX,mouseY,160,260,122,203) and inputs:#1
        mtn(1)
        print("1 has been added")
        
    if button(mouseX,mouseY,270,370,122,203) and inputs:#2
        mtn(2)
        print("2 has been added")
        
    if button(mouseX,mouseY,380,480,122,203) and inputs:#3
        mtn(3)
        print("3 has been added")
            
    if button(mouseX,mouseY,160,260,211,290) and inputs:#4
        mtn(4)
        print("4 has been added")
        
    if button(mouseX,mouseY,270,370,211,290) and inputs:#5
        mtn(5)
        print("5 has been added")
        
    if button(mouseX,mouseY,380,480,211,290) and inputs:#6
        mtn(6)
        print("6 has been added")

    if button(mouseX,mouseY,160,260,300,376) and inputs:#7
        mtn(7)
        print("7 has been added")
        
    if button(mouseX,mouseY,270,370,300,376) and inputs:#8
        mtn(8)
        print("8 has been added")
        
    if button(mouseX,mouseY,380,480,300,376) and inputs:#9
        mtn(9)
        print("9 has been added")
        
    if button(mouseX,mouseY,10,110,77,160) and more_than_number != "" and sy_inputs:# +
        mtn("+")
        print("+ has been added")
        inputs = True
        sy_inputs = False



    if button(mouseX,mouseY,10,110,165,245) and more_than_number != "" and sy_inputs:# -
        mtn("-")
        print("- has been added")
        inputs = True
        sy_inputs = False


    if button(mouseX,mouseY,10,110,253,332) and more_than_number != "" and sy_inputs:# *
        mtn("*")
        print("* has been added")
        inputs = True
        sy_inputs = False
        

    if button(mouseX,mouseY,10,110,340,420) and more_than_number != "" and sy_inputs:# /
        mtn("/")
        print("/ has been added")
        inputs = True
        sy_inputs = False
        

    if button(mouseX,mouseY,10,110,425,495):# =
        processor(more_than_number)
        

    if button(mouseX,mouseY,140,240,427,496):# Clear button
        clear_function()
        
        
        
        
        
        
def keyPressed():
    clicking(key) # adding numbers (It works with the numpad numbers)
    #print(keyCode) Remove "#" if you want to know the keyCode number of any key
    # 8 = backspace, 127 = DEL
    if keyCode == 8 or keyCode == 127: # clear when pressed DEL and BACKSPACE 
        clear_function()
        
    if keyCode == 10:# Get the result when pressed ENTER
        clicking("=")
        
        
        
        
        
