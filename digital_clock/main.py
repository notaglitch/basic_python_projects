import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S: %p')
    label.config(text=current_time)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry('500x200')
root.config(bg="black")

label = tk.Label(root, font=('Arial', 50, 'bold'),bg="black", fg="#00FF00")
label.pack(anchor='center', pady=60)

time()
root.mainloop()
