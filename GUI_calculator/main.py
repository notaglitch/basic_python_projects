import tkinter as tk

# Function to update the input field
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying expressions
entry = tk.Entry(root, width=25, font=("Arial", 14), borderwidth=5, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout and configuration
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=clear)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
