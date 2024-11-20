import turtle

screen = turtle.Screen()
screen.bgcolor("cyan")

tonyTurtle = turtle.Turtle()
tonyTurtle.color("Deep Pink")


def hexagon(size):
    for i in range(6):
        tonyTurtle.fd(size)
        tonyTurtle.left(60)
        size = size + 5

hexagon(6)
hexagon(24)
hexagon(96)
hexagon(200)