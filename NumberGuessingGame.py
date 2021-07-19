import tkinter as tk
import random

root = tk.Tk()
root.title("Guessing Number Game")
root.geometry("700x700")
root.resizable(0, 0)

number = random.randint(1, 10)
print("The mystery number is", number)  # Print The mystery number

attempt = 3

game_end = False

# Function


def guess(g_number):
    global number, attempt, game_end

    # Check for game is end
    if g_number == number and attempt != 0 and not(game_end):
        all_buttons[g_number - 1].config(bg="dark cyan", fg="white")
        label_number.config(text="WELL GUESSED !!")
        game_end = True

    elif g_number != number and attempt > 0 and not(game_end):
        all_buttons[g_number - 1].config(fg="white")
        attempt -= 1
        label_attempt.config(text="ATTEMPT : " + str(attempt))

        if attempt == 2:
            label_attempt.config(bg="#E8DA10")  # bg = Yellow
            if g_number < number:
                label_number.config(text="IT'S GREATER THAN THAT")
            else:
                label_number.config(text="IT'S LESS THAN THAT")

        elif attempt == 1:
            label_attempt.config(bg="#B80028")  # bg = Red
            if g_number < number:
                label_number.config(text="IT'S GREATER THAN THAT")
            else:
                label_number.config(text="IT'S LESS THAN THAT")

        elif attempt == 0:
            label_attempt.config(bg="black", fg="white")
            all_buttons[number - 1].config(bg="dark cyan", fg="white")
            label_number.config(text="THAT'S THE NUMBER")
            game_end = True


# Row 1 - 4
row1 = tk.Frame(root)
row1.pack(expand=True, fill="both")
row2 = tk.Frame(root)
row2.pack(expand=True, fill="both")
row3 = tk.Frame(root)
row3.pack(expand=True, fill="both")
row4 = tk.Frame(root)
row4.pack(expand=True, fill="both")


# Row 1
label_number = tk.Label(
    row1, font=("Arial", 29, "bold"), text="GUESS THE NUMBER !!")
label_number.pack(expand=True, fill="both")

# Row 2
button1 = tk.Button(row2, text=1, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(1))
button1.pack(side="left", expand=True, fill="both")
button2 = tk.Button(row2, text=2, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(2))
button2.pack(side="left", expand=True, fill="both")
button3 = tk.Button(row2, text=3, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(3))
button3.pack(side="left", expand=True, fill="both")
button4 = tk.Button(row2, text=4, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(4))
button4.pack(side="left", expand=True, fill="both")
button5 = tk.Button(row2, text=5, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(5))
button5.pack(side="left", expand=True, fill="both")


# Row 3
button6 = tk.Button(row3, text=6, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(6))
button6.pack(side="left", expand=True, fill="both")
button7 = tk.Button(row3, text=7, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(7))
button7.pack(side="left", expand=True, fill="both")
button8 = tk.Button(row3, text=8, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(8))
button8.pack(side="left", expand=True, fill="both")
button9 = tk.Button(row3, text=9, font=("Arial", 40, "bold"), bd=0,
                    bg="white", command=lambda: guess(9))
button9.pack(side="left", expand=True, fill="both")
button10 = tk.Button(row3, text=10, font=("Arial", 40, "bold"), bd=0,
                     bg="white", command=lambda: guess(10))
button10.pack(side="left", expand=True, fill="both")


# Row 4
label_attempt = tk.Label(row4, text="ATTEMPT : " + str(attempt),
                         bd=0, font=("Arial", 29, "bold"), bg="#35AD00", fg="white")  # bg = Green
label_attempt.pack(side="left", expand=True, fill="both")

# Make a list of all buttons
all_buttons = [button1, button2, button3, button4, button5,
               button6, button7, button8, button9, button10]

root.mainloop()
