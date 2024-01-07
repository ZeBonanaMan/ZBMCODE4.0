import tkinter as tk
from tkinter import font

def calculate():
    num_1 = number1_entry.get()
    num_2 = number2_entry.get()
    num_3 = number3_entry.get()

    try:
        #phase1
        if float(num_1) <= float(num_2):
            temp_biggest = num_2

            #phase2
            if float(temp_biggest) <= float(num_3):
                    temp_biggest = num_3
                    display_label.config(text=f"The biggest value is: {temp_biggest}")
            else:
                display_label.config(text=f"The biggest value is: {temp_biggest}")
        else: 
            temp_biggest = num_1
            if float(temp_biggest) <= float(num_3):
                    temp_biggest = num_3
                    display_label.config(text=f"The biggest value is: {temp_biggest}")
            else:
                display_label.config(text=f"The biggest value is: {temp_biggest}")

    except ValueError:
        display_label.config(text="Please input valid values")

win=tk.Tk()
win.title("Biggest Number Calculator")
win.geometry("500x350")

#darkmode parameters
bg_color = "#2a2a2a"
fg_color = "#FFFFFF"
num_1_color = "#ed2939"
num_2_color = "#3cb043"
num_3_color = "#F28500"
label_color = "#2d9dbd"
input_bg_color = "#545454"

win.config(bg=bg_color)

final_font = font.Font(size=20)

spacer = tk.Label(bg=bg_color)
spacer.pack()

title_label = tk.Label(text="Which is the biggest?", bg=bg_color, fg=fg_color, font=final_font)
title_label.pack()

number1_label = tk.Label()
number1_label.pack
number1_entry = tk.Entry(bg=input_bg_color, fg=num_1_color, font=final_font, justify= "center")
number1_entry.pack()

spacer = tk.Label(bg=bg_color)
spacer.pack()

number2_label = tk.Label()
number2_label.pack
number2_entry = tk.Entry(bg=input_bg_color, fg=num_2_color, font=final_font, justify= "center")
number2_entry.pack()

spacer = tk.Label(bg=bg_color)
spacer.pack()

number3_label = tk.Label()
number3_label.pack
number3_entry = tk.Entry(bg=input_bg_color, fg=num_3_color, font=final_font, justify= "center")
number3_entry.pack()

spacer = tk.Label(bg=bg_color)
spacer.pack()

calculate_button = tk.Button(bg=bg_color, fg=fg_color, text="Calculate", command=calculate,)
calculate_button.pack()

spacer = tk.Label(bg=bg_color)
spacer.pack()

display_label = tk.Label(bg=bg_color, fg=label_color, font=final_font)
display_label.pack()

win.mainloop()