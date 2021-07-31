from scoreboard import Scoreboard
import turtle as t
import time
from snake import Snake
from food import Food

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.addScore()

    # Detect collision with wall
    xAxisCollide = snake.head.xcor() < -280 or snake.head.xcor() > 280
    yAxisCollide = snake.head.ycor() < -280 or snake.head.ycor() > 280
    if xAxisCollide or yAxisCollide:
        scoreboard.gameover()
        gameIsOn = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.gameover()
            gameIsOn = False

screen.exitonclick()
