from turtle import Turtle, Screen
import OOP_review

OOP_review.reverie.poodleFurz("floof")

towanda = Turtle()
towanda.shape("turtle")
towanda.color("dark magenta")
towanda.setpos(50,50)
towanda.left(100)
towanda.forward(35)
towanda.stamp()
towanda.right(80)
towanda.forward(95)
towanda.circle(90,500)
towanda.forward(100)

print(towanda)

myScreen = Screen()
print(myScreen.canvheight)
myScreen.exitonclick()