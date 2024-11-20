from turtle import *

trinity = Turtle()

for steps in range(100):
    for c in ("cyan4","DeepPink","DarkViolet"):
        color(c)
        forward(steps)
        right(30)

screen = Screen()

screen.exitonclick()

