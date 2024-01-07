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
win.title("if-else statement")
win.geometry("1000x1000")

#darkmode parameters
bg_color = "#2a2a2a"
fg_color = "#FFFFFF"
label_color = "#2d9dbd"
input_bg_color = "#545454"

win.config(bg=bg_color)

number1_label = tk.Label()
number1_label.pack
number1_entry = tk.Entry()
number1_entry.pack()

number2_label = tk.Label()
number2_label.pack
number2_entry = tk.Entry()
number2_entry.pack()

number3_label = tk.Label()
number3_label.pack
number3_entry = tk.Entry()
number3_entry.pack()

calculate_button = tk.Button(text="Calculate", command=calculate,)
calculate_button.pack()

display_label = tk.Label(bg=bg_color)
display_label.pack()

win.mainloop()