import turtle as t

colors = ['red', 'purple', 'blue', 'orange']
t.bgcolor('black')
t.speed(10)
for i in range(200):
    for c in range(len(colors)):
        t.pencolor(colors[c])
        t.forward(i)
        t.left(59)
