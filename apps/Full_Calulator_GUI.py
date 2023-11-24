import tkinter as tk
import math

def evaluate_expression():
    try:
        expression = entry.get()
        # Replace trigonometric and logarithmic functions in the expression
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)

def button_click(char):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + char)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for input and output
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+',
    'sin', 'cos', 'tan',
    'log', 'ln', '(', ')',
    # Moved the "=" button to the end
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create clear and evaluate buttons
tk.Button(root, text="C", width=5, height=2, command=clear_entry).grid(row=5, column=0)
# The "=" button is now at the end of the buttons list
tk.Button(root, text="=", width=5, height=2, command=evaluate_expression).grid(row=5, column=3)

root.mainloop()
