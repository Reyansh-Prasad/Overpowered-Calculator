import tkinter as tk
import math

# Function to update the expression in the entry field
def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry field
def clear():
    entry_var.set("")

# Function for square root
def sqrt():
    try:
        result = math.sqrt(float(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Create GUI window
root = tk.Tk()
root.title("Overpowered Calculator")
root.geometry("300x400")

# Entry field to display input & results
entry_var = tk.StringVar()
entry_field = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right")
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('√', 5, 1)
]

# Adding buttons to the window
for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    elif text == 'C':
        action = clear
    elif text == '√':
        action = sqrt
    else:
        action = lambda t=text: press(t)

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=action).grid(row=row, column=col)

# Run the application
root.mainloop()
