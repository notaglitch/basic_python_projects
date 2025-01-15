import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.config(bg="#333333")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, relief="sunken", justify="right", bd=10, fg="white", bg="#444444")
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

button_style = {
    'width': 5,
    'height': 2,
    'font': ("Arial", 18),
    'relief': "flat",
    'bd': 3,
    'fg': "white",
    'bg': "#555555",
    'activebackground': "#888888",
    'activeforeground': "black"
}

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, **button_style, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, **button_style, command=clear)
    else:
        button = tk.Button(root, text=text, **button_style, command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=10, pady=10)

root.mainloop()
