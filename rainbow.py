from turtle import *
from time import *
import turtle
t = Turtle()
t.speed(1)
t.pensize(4)
turtle.bgcolor("black")
colors = ["red", "yellow", "green", "blue"]
t._tracer(False)
for a in range(400):
    t.forward(2*a)
    t.color(colors[a % 4])
    t.left(91)

