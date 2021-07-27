from turtle import Turtle, Screen
import random
# import colorgram

# colors = colorgram.extract("image.jpg", 30)

# rgb_color = []
# for i in range(len(colors)):
#     rgb = colors[i].rgb  # e.g. (255, 151, 210)
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     rgb_color.append((r, g, b))

color_list = [(43, 94, 148), (179, 45, 76), (226, 208, 101), (208, 156, 87), (139, 89, 62), (178, 169, 33), (117, 177, 207), (200, 76, 124), (212, 129, 173), (228, 69, 49), (94, 101, 188), (128, 38, 65), (25, 147, 86),
              (53, 165, 113), (51, 55, 93), (124, 217, 207), (116, 46, 36), (29, 180, 190), (230, 168, 186), (120, 191, 173), (174, 186, 222), (49, 52, 68), (83, 43, 33), (154, 206, 215), (236, 170, 159), (211, 206, 39)]

turtle = Turtle()

turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()

screen = Screen()
screen.colormode(255)

startingPoint = (-300, -275)
gap = 60
yAxis = startingPoint[1]
for i in range(10):
    xAxis = startingPoint[0]
    for j in range(11):
        turtle.setpos(xAxis, yAxis)
        turtle.dot(30, random.choice(color_list))
        xAxis += gap
    yAxis += gap
    turtle.setpos(0, yAxis)

screen.exitonclick()
