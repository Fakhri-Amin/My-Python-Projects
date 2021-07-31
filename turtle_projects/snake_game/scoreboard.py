import turtle
FONT = ("courier", 20, "bold")
ALIGNMENT = "center"


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.updateScore()

    def updateScore(self):
        self.write(f"SCORE : {self.score}", font=FONT, align=ALIGNMENT)

    def addScore(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def gameover(self):
        self.home()
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
