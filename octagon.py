import turtle
import random
turtle.speed(10)
turtle.pensize(5)
scr = turtle.Screen()
scr.colormode(255)
scr.bgcolor("black")
def octagon(size):
    for side in range(8):
        turtle.forward(size)
        turtle.left(45)

rand_color = random.choices(range(256), k=3)

octagon(1)
count = 0
colours = ["cyan", "purple", "white", "blue"]

while count < 1000:
    for side in range(6):
        
        turtle.penup()
        turtle.left(60)
        turtle.forward(10)
        turtle.pendown()
        octagon(count)
        turtle.color(random.choice(colours))
    count=count+10;
    
    

    


    


    
    