import random
import turtle

turtle.bgcolor("black")
i = 1
while i<300:
    

    r = random.randint(0,255) 
    g = random.randint(0,255) 
    b = random.randint(0,255) 


    turtle.colormode(255)
    turtle.pencolor(r,g,b)
    turtle.forward(50+i)
    turtle.right(90.9)

    i = i +1
