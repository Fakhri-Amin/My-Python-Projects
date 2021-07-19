import tkinter as tk
import random

root = tk.Tk()
root.geometry("600x750")
root.title("Rock Scissor Paper")

offColor = "light gray"
textColor = "white"

font = "Arial"

game_end = False

choices = ["rock", "scissor", "paper"]


def call(player_call):
    global game_end
    if game_end is False:
        game_end = True
        com_call = random.choice(choices)
        label_vs.config(text="RESTART ?", font=(font, 30, "bold"))
        if player_call == "rock":
            if com_call == "rock":
                player_label.config(text="DRAW")
                computer_label.config(text="DRAW")

                player_paper.config(bg=offColor, fg=offColor)
                player_scissor.config(bg=offColor, fg=offColor)
                computer_paper.config(bg=offColor, fg=offColor)
                computer_scissor.config(bg=offColor, fg=offColor)

            if com_call == "scissor":
                player_label.config(text="YOU WIN")
                computer_label.config(text="COMPUTER LOSES")

                player_paper.config(bg=offColor, fg=offColor)
                player_scissor.config(bg=offColor, fg=offColor)
                computer_paper.config(bg=offColor, fg=offColor)
                computer_rock.config(bg=offColor, fg=offColor)

            if com_call == "paper":
                player_label.config(text="YOU LOSE")
                computer_label.config(text="COMPUTER WINS")

                player_paper.config(bg=offColor, fg=offColor)
                player_scissor.config(bg=offColor, fg=offColor)
                computer_scissor.config(bg=offColor, fg=offColor)
                computer_rock.config(bg=offColor, fg=offColor)

        elif player_call == "paper":
            if com_call == "rock":
                player_label.config(text="YOU WIN")
                computer_label.config(text="COMPUTER LOSES")

                player_rock.config(bg=offColor, fg=offColor)
                player_scissor.config(bg=offColor, fg=offColor)
                computer_paper.config(bg=offColor, fg=offColor)
                computer_scissor.config(bg=offColor, fg=offColor)

            if com_call == "scissor":
                player_label.config(text="YOU LOSE")
                computer_label.config(text="COMPUTER WINS")

                player_rock.config(bg=offColor, fg=offColor)
                player_scissor.config(bg=offColor, fg=offColor)
                computer_paper.config(bg=offColor, fg=offColor)
                computer_rock.config(bg=offColor, fg=offColor)

            if com_call == "paper":
                player_label.config(text="DRAW")
                computer_label.config(text="DRAW")

                player_rock.config(bg=offColor, fg=offColor)
                player_scissor.config(bg=offColor, fg=offColor)
                computer_rock.config(bg=offColor, fg=offColor)
                computer_scissor.config(bg=offColor, fg=offColor)

        elif player_call == "scissor":
            if com_call == "rock":
                player_label.config(text="YOU LOSE")
                computer_label.config(text="COMPUTER WINS")

                player_paper.config(bg=offColor, fg=offColor)
                player_rock.config(bg=offColor, fg=offColor)
                computer_paper.config(bg=offColor, fg=offColor)
                computer_scissor.config(bg=offColor, fg=offColor)

            if com_call == "scissor":
                player_label.config(text="DRAW")
                computer_label.config(text="DRAW")

                player_paper.config(bg=offColor, fg=offColor)
                player_rock.config(bg=offColor, fg=offColor)
                computer_paper.config(bg=offColor, fg=offColor)
                computer_rock.config(bg=offColor, fg=offColor)

            if com_call == "paper":
                player_label.config(text="YOU WIN")
                computer_label.config(text="COMPUTER LOSES")

                player_paper.config(bg=offColor, fg=offColor)
                player_rock.config(bg=offColor, fg=offColor)
                computer_scissor.config(bg=offColor, fg=offColor)
                computer_rock.config(bg=offColor, fg=offColor)


def clear():
    global game_end
    game_end = False
    player_label.config(text="PLAYER")
    computer_label.config(text="COMPUTER")
    label_vs.config(text="VS", font=(font, 30, "bold"))

    player_rock.config(bg="#B80028", fg="white")
    computer_rock.config(bg="#B80028", fg="white")

    player_scissor.config(bg="#35AD00", fg="white")
    computer_scissor.config(bg="#35AD00", fg="white")

    player_paper.config(bg="#0a44a1", fg="white")
    computer_paper.config(bg="#0a44a1", fg="white")


# Row 1 - 5
row1 = tk.Frame(root,)
row2 = tk.Frame(root)
row3 = tk.Frame(root)
row4 = tk.Frame(root)
row5 = tk.Frame(root)

row1.pack(expand=True, fill="both")
row2.pack(expand=True, fill="both")
row3.pack(expand=True, fill="both")
row4.pack(expand=True, fill="both")
row5.pack(expand=True, fill="both")

# Row 1 : Win or Lose (Computer)
computer_label = tk.Label(row1, text="COMPUTER", font=(
    font, 30, "bold"), bg="white", fg="black")
computer_label.pack(expand=True, fill="both")

# Row 2 : Computer Button
computer_rock = tk.Button(row2, text="ROCK", font=(
    font, 20, "bold"), bd=0, bg="#B80028", fg="white")
computer_scissor = tk.Button(row2, text="SCISSOR", font=(
    font, 20, "bold"), bd=0, bg="#35AD00", fg="white")
computer_paper = tk.Button(row2, text="PAPER", font=(
    font, 20, "bold"), bd=0, bg="#0a44a1", fg="white")

computer_rock.pack(side="left", expand=True, fill="both")
computer_scissor.pack(side="left", expand=True, fill="both")
computer_paper.pack(side="left", expand=True, fill="both")

# Row 3 : Label VS
label_vs = tk.Button(row3, text="VS", font=(
    font, 35, "bold"), bg="white", fg="black", command=clear, bd=0)
label_vs.pack(expand=True, fill="both")

# Row 4 : Player Button
player_rock = tk.Button(row4, text="ROCK", font=(
    font, 20, "bold"), bd=0, command=lambda: call("rock"), bg="#B80028", fg="white")
player_scissor = tk.Button(row4, text="SCISSOR", font=(
    font, 20, "bold"), bd=0, command=lambda: call("scissor"), bg="#35AD00", fg="white")
player_paper = tk.Button(row4, text="PAPER", font=(
    font, 20, "bold"), bd=0, command=lambda: call("paper"), bg="#0a44a1", fg="white")

player_rock.pack(side="left", expand=True, fill="both")
player_scissor.pack(side="left", expand=True, fill="both")
player_paper.pack(side="left", expand=True, fill="both")

# Row 5 : Win or Lose (Player)
player_label = tk.Label(row5, text="PLAYER", font=(
    font, 30, "bold"), bg="white", fg="black")
player_label.pack(expand=True, fill="both")

root.mainloop()
