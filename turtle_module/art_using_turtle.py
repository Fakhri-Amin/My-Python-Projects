from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.shape("turtle")
turtle.color("crimson")

screen = Screen()
screen.colormode(255)


#! Draw a sqaure
# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

#! Draw a dashed line
# for i in range(8):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

#! Draw a triangle, pentagon, and so on..
# ? Way 1
# sides = 3
# colors = ["red", "green", "blue", "black"]
# while True:
#     angle = 360 / sides
#     for i in range(sides):
#         turtle.forward(100)
#         turtle.right(angle)
#     sides += 1
#     turtle.color(random.choice(colors))
#     if sides == 11:
#         break

# ? Way 2
# colors = ["red", "green", "blue", "black"]
# turtle.hideturtle()
# turtle.pensize(3)


# def draw_shape(sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         turtle.forward(100)
#         turtle.right(angle)


# for i in range(3, 11):
#     turtle.color(random.choice(colors))
#     draw_shape(i)

screen.exitonclick()
