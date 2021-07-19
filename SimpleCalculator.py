from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("500x740")
root.resizable(0, 0)

text = StringVar()
calculation = ""


def button_click(number):
    global calculation
    calculation = calculation + str(number)
    text.set(calculation)


def button_clear():
    global calculation
    calculation = ""
    text.set("")


def button_equal():
    global calculation
    try:
        result = str(eval(calculation))
        text.set(result)
        calculation = ""
    except:
        text.set("ERROR")
        calculation = ""


def button_backspace():
    global calculation
    lastIndex = len(calculation) - 1
    calculation = calculation[:lastIndex]
    text.set(calculation)


label = Label(
    root,
    text="A",
    font=("Arial", 70),
    bg="black",
    fg="black"
)
label.pack(expand=True, fill="both")

label = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Arial", 43),
    textvariable=text,
    bg="black",
    fg="white"
)
label.pack(expand=True, fill="both")

# ROWS 1 - 5
row1 = Frame(root)
row1.pack(expand=True, fill="both")

row2 = Frame(root)
row2.pack(expand=True, fill="both")

row3 = Frame(root)
row3.pack(expand=True, fill="both")

row4 = Frame(root)
row4.pack(expand=True, fill="both")

row5 = Frame(root)
row5.pack(expand=True, fill="both")

# ROW 1
button_clear = Button(row1, text=" C ", font=(
    "Arial", 26), command=button_clear, bg="#d1d1d1", border=0)
button_clear.pack(side=LEFT, expand=True, fill="both")

button_backspace = Button(row1, text="CE", font=(
    "Arial", 25), command=button_backspace, bg="#d1d1d1", border=0)
button_backspace.pack(side=LEFT, expand=True, fill="both")

button_modulus = Button(row1, text="%", font=(
    "Arial", 30), command=lambda: button_click("%"), bg="#d1d1d1", border=0)
button_modulus.pack(side=LEFT, expand=True, fill="both")

button_divide = Button(
    row1, text=" / ", font=("Arial", 32), command=lambda: button_click("/"), bg="#ff8000", fg="white", border=0)
button_divide.pack(side=LEFT, expand=True, fill="both")

# ROW 2
button7 = Button(row2, text="7", font=("Arial", 29),
                 command=lambda: button_click(7), border=0, activebackground="#d1d1d1")
button7.pack(side=LEFT, expand=True, fill="both")

button8 = Button(row2, text="8", font=("Arial", 29),
                 command=lambda: button_click(8), border=0, activebackground="#d1d1d1")
button8.pack(side=LEFT, expand=True, fill="both")

button9 = Button(row2, text="9", font=("Arial", 29),
                 command=lambda: button_click(9), border=0, activebackground="#d1d1d1")
button9.pack(side=LEFT, expand=True, fill="both")

button_multiply = Button(row2, text="x", font=("Arial", 30),
                         command=lambda: button_click("*"), bg="#ff8000", fg="white", border=0)
button_multiply.pack(side=LEFT, expand=True, fill="both")

# ROW 3
button4 = Button(row3, text="4", font=("Arial", 28),
                 command=lambda: button_click(4), border=0, activebackground="#d1d1d1")
button4.pack(side=LEFT, expand=True, fill="both")

button5 = Button(row3, text="5", font=("Arial", 28),
                 command=lambda: button_click(5), border=0, activebackground="#d1d1d1")
button5.pack(side=LEFT, expand=True, fill="both")

button6 = Button(row3, text="6", font=("Arial", 28),
                 command=lambda: button_click(6), border=0, activebackground="#d1d1d1")
button6.pack(side=LEFT, expand=True, fill="both")

button_substract = Button(
    row3, text="-", font=("Arial", 33), command=lambda: button_click("-"), bg="#ff8000", fg="white", border=0)
button_substract.pack(side=LEFT, expand=True,
                      fill="both")

# ROW 4
button1 = Button(row4, text="1", font=("Arial", 29),
                 command=lambda: button_click(1), border=0, activebackground="#d1d1d1")
button1.pack(side=LEFT, expand=True, fill="both")

button2 = Button(row4, text="2", font=("Arial", 29),
                 command=lambda: button_click(2), border=0, activebackground="#d1d1d1")
button2.pack(side=LEFT, expand=True, fill="both")

button3 = Button(row4, text="3", font=("Arial", 29),
                 command=lambda: button_click(3), border=0, activebackground="#d1d1d1")
button3.pack(side=LEFT, expand=True, fill="both")

button_add = Button(row4, text="+", font=("Arial", 28),
                    command=lambda: button_click("+"), bg="#ff8000", fg="white", border=0)
button_add.pack(side=LEFT, expand=True, fill="both")

# ROW 5
button_point = Button(row5, text=".", font=("Arial", 33),
                      command=lambda: button_click("."), border=0, activebackground="#d1d1d1")
button_point.pack(side=LEFT, expand=True, fill="both")

button0 = Button(row5, text="0", font=("Arial", 27),
                 command=lambda: button_click(0), border=0, activebackground="#d1d1d1")
button0.pack(side=LEFT, expand=True, fill="both")

button_equal = Button(row5, text="=", font=("Arial", 27),
                      command=button_equal, border=0, activebackground="#d1d1d1")
button_equal.pack(side=LEFT, expand=True, fill="both")

button_square = Button(row5, text="^", font=("Arial", 28),
                       command=lambda: button_click("**"), bg="#ff8000", fg="white", border=0)
button_square.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
