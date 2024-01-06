import tkinter as tk
from tkinter import font


def biggest_num():
    try:
        num1 = input()
        num2 = input()
        num3 = input()

    except ValueError:
        display_label.config(text="Please enter a valid number.")

win=tk.Tk()
win.title("if-else statement")
win.geometry("1000x1000")

#darkmode parameters
bg_color = "#2a2a2a"
fg_color = "#FFFFFF"
label_color = "#2d9dbd"
input_bg_color = "#545454"
button_bg_color = "#2a2a2a"
apple_color = "#ed2939"
money_color  ="#3cb043"

win.config(bg=bg_color)

display_label = tk.Label(bg=bg_color)
display_label.pack()

win.mainloop()