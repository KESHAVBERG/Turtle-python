import turtle as t

t.bgcolor('black')
t.pensize(2)
t.speed(10)

colors = ['red','yellow','green','white']

for i in range(100):
    for c in range(len(colors)):
        t.color(colors[c])
        t.circle(100)
        t.left(10)
