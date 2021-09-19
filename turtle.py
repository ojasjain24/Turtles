import turtle
import math
bob = turtle.Turtle()
bob.getscreen().bgcolor("cyan")
bob.speed(10)
bob.color("red","yellow")
bob.begin_fill()
for i in range(50):
    bob.forward(200)
    bob.left(170)
bob.forward(100)
bob.end_fill()
bob.color("green")
for i in range(10):
    bob.forward(math.sqrt(i)*10)
    bob.left(i)
bob.right(135)
bob.color("green")
for i in range(10):
    bob.forward(math.sqrt(i)*10)
    bob.left(i)

bob.color("red","yellow")
bob.begin_fill()
for i in range(50):
    bob.forward(200)
    bob.left(170)
bob.forward(100)
bob.end_fill()
turtle.done()
