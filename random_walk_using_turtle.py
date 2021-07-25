from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("crimson")

screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    aTuple = (r, g, b)
    return aTuple


turtle.hideturtle()
turtle.pensize(15)
turtle.speed("fastest")
dirs = [0, 90, 180, 270]

for i in range(500):
    turtle.setheading(random.choice(dirs))
    turtle.forward(30)
    turtle.color(random_color())

screen.exitonclick()
