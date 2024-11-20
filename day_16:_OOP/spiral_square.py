import turtle

screen = turtle.Screen()
screen.bgcolor("cyan")

tonyTurtle = turtle.Turtle()
tonyTurtle.color("Deep Pink")


def square(size):
    for i in range(4):
        tonyTurtle.fd(size)
        tonyTurtle.left(90)
        size = size + 15

square(6)
square(48)
square(96)