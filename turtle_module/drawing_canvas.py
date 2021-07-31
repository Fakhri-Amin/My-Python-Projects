import turtle as t

turtle = t.Turtle()

screen = t.Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def turn_left():
    turtle.left(10)


def turn_right():
    turtle.right(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.onkeypress(fun=move_forward, key="w")
screen.onkeypress(fun=move_backward, key="s")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=clear, key="c")
screen.listen()

screen.exitonclick()
