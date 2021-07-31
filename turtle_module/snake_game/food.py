import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomX = random.randint(-240, 240)
        randomY = random.randint(-240, 240)
        self.goto(randomX, randomY)
