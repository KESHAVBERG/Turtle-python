Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.bgcolor('black')
>>> turtle.speed(5)
>>> colors = ['red', 'cyan', 'white','green']
>>> for i in range(100):
	for c in range(len(colors)):
		turtle.color(colors[c])
		turtle.circle(100)
		turtle.left(10)

		

