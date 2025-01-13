import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry('500x250')
root.config(bg="#2E3B55")

label = tk.Label(root, font=('Segoe UI', 50, 'bold'), background="#2E3B55", foreground="#00FF00")
label.pack(anchor='center', pady=60)

time()
root.mainloop()
