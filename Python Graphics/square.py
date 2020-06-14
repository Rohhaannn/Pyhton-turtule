import turtle

my_turtle = turtle.Turtle()

def square(length, angle):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.right(angle)

for j in range(1000):
    square(100, 90)
    my_turtle.right(13)
