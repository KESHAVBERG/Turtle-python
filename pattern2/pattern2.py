import turtle as t

colors = ['red', 'green','yellow', 'cyan']
t.bgcolor('black')
t.pensize(10)
t.hideturtle()
for x in range(0,2):
    angle = x*100
for i in range(0,100):
    for b in range(0,2):
        for c in range(len(colors)):
            t.pencolor(colors[c])
            t.forward(100+i*2)
            t.right(angle+b)


            
