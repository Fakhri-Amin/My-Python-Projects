import turtle
import time
import random

WIDTH, HEIGHT = 600, 600
color_list = ["red", "blue", "yellow", "cyan", "purple",
              "green", "black", "brown", "orange", "pink"]


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10) : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric...Try Again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number is not in range...Try Again!")


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.pensize(4)
        racer.shapesize(1.2)
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 30)
        racer.pendown()
        turtles.append(racer)

    return turtles


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)

            y = racer.pos()[1]
            if y >= HEIGHT // 2 - 43:
                return colors[turtles.index(racer)]


def init_turtle():
    global screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Racing Turtle")
    screen.colormode(255)


def draw_finish_line():
    referee = turtle.Turtle()
    time.sleep(1)
    referee.speed("slow")
    referee.hideturtle()
    referee.penup()
    referee.pensize(4)
    referee.setpos(-WIDTH // 2, HEIGHT // 2 - 30)
    referee.pendown()
    referee.forward(HEIGHT)


def draw_score():
    score = turtle.Turtle()
    score.color(winner)
    score.hideturtle()
    score.penup()
    score.setpos(0, HEIGHT // 2 - 27)
    score.pendown()
    style = ("arial", 15, "bold")
    score.write(f"THE WINNER IS THE {winner.upper()} TURTLE",
                font=style, align='center')


# STARTING FLOW
racers = get_number_of_racers()
init_turtle()
draw_finish_line()
random.shuffle(color_list)
colors = color_list[:racers]
winner = race(colors)
draw_score()

screen.exitonclick()
