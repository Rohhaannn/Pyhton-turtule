import turtle

colors=['red', 'purple', 'blue', 'green','orange', 'yellow']
t= turtle.Pen()
turtle.bgcolor('Black')

for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(50)

turtle.done()
