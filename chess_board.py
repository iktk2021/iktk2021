import turtle

import time
import random
color_list=['blue','white']
drawer=turtle.Turtle()
space=0
y=-100

for i in range(5):
    
    drawer.penup()
    drawer.goto(-100,y)
    drawer.pendown()
    for i in range(5):
       
        
        if space%2==0:
            drawer.fillcolor('black')
        else:
            drawer.fillcolor('white')
        drawer.begin_fill()
        for i in range(4):
           drawer.forward(30)
           drawer.right(90)
       
        drawer.end_fill()
        space=space+1  
        drawer.forward(30)
        
        
        print(space)
        
    y+=30
   
time.sleep(20)
