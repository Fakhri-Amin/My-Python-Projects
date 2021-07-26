from turtle import Turtle, Screen
import random

turtle = Turtle()

turtle.pensize(3)
turtle.speed("fastest")
turtle.hideturtle()

screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    aTuple = (r, g, b)
    return aTuple


def draw_circle(sizeOfGap, sizeOfCircle):
    for _ in range(int(360 / sizeOfGap)):
        turtle.color(random_color())
        turtle.circle(sizeOfCircle)
        turtle.setheading(turtle.heading() + sizeOfGap)


draw_circle(10, 120)
draw_circle(12, 100)
draw_circle(14, 70)

screen.exitonclick()
