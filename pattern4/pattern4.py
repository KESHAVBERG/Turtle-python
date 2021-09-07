import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.pencolor('red')
t.hideturtle()

t.penup()  
t.goto(0,200)  
t.pendown()


a = 0
b = 0
while(True):
    t.forward(a)
    t.right(b)

    a += 3
    b += 1

    if b==200:
        break


turtle.done()
    
