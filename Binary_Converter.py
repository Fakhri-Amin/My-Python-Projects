import pyperclip
import tkinter as tk

root = tk.Tk()
root.title("Text To Binary Converter")
root.resizable(0, 0)

input_text = tk.StringVar()
result = ""


def stringToBinary(text):
    global result
    result = ""
    for i in text:
        if i.isalpha():
            result = result + format(ord(i), "b")
        else:
            result = result + "0" + format(ord(i), "b")
    input_text.set(result)


def BinaryToString(text):
    global result
    result = ""
    for i in range(0, len(text), 7):
        binaryNumbers = text[i:i + 7]
        integerData = int(binaryNumbers, 2)
        result = result + chr(integerData)
    input_text.set(result)


def copy():
    pyperclip.copy(result)


def clear():
    entry.delete(0, tk.END)


# Canvas
canvas = tk.Canvas(root, height=770, width=710, bg="#4d1919")
canvas.pack()

# Frame
upperFrame = tk.Frame(root, bg="#bf4040", bd=7)
upperFrame.place(relx=0.5, rely=0.04, relwidth=0.9,
                 relheight=0.06, anchor="n")

lowerFrame = tk.Frame(root, bg="#bf4040", bd=7)
lowerFrame.place(relx=0.5, rely=0.2, relwidth=0.9, relheight=0.67, anchor="n")

# Entry
entry = tk.Entry(upperFrame, font=("Arial", 18),
                 border=0, selectbackground="gray", width=540)
entry.place(relwidth=0.92)

# Button
button_encode = tk.Button(root, text="Encode", font=("Arial", 15),
                          border=0, command=lambda: stringToBinary(entry.get()), activebackground="gray")
button_encode.place(relx=0.3, rely=0.12, relwidth=0.3,
                    relheight=0.05, anchor="n")

button_decode = tk.Button(root, text="Decode", font=("Arial", 15),
                          border=0, command=lambda: BinaryToString(entry.get()), activebackground="gray")
button_decode.place(relx=0.7, rely=0.12, relwidth=0.3,
                    relheight=0.05, anchor="n")

button_copy = tk.Button(root, text="Copy", font=("Arial", 15),
                        border=0, command=copy, activebackground="gray")
button_copy.place(relx=0.5, rely=0.9, relwidth=0.3,
                  relheight=0.05, anchor="n")

button_clear = tk.Button(upperFrame, text="X",
                         command=clear, bd=0, font=("Arial", 18), bg="#bf4040", fg="white")
button_clear.place(relx=0.93, relheight=1, relwidth=0.07)

# Label
lowerLabel = tk.Label(lowerFrame, bg="white")
lowerLabel.place(relwidth=1, relheight=1)

insideLabel = tk.Label(lowerLabel, textvariable=input_text,
                       font=("Arial", 22), anchor="nw", wraplength=700, justify="left")
insideLabel.place(relwidth=1, relheight=1)

root.mainloop()
