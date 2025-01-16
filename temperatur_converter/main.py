import tkinter as tk
from tkinter import messagebox

def getTemp():
    try:
        temp = float(entry_temp.get())
        return temp
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid temperature.")
        return None

def convert_to_celsius():
    temp = getTemp()
    if temp is not None:
        converted = round((temp - 32) * 5/9, 2)
        label_result.config(text=f"Converted: {converted} °C")

def convert_to_fahrenheit():
    temp = getTemp()
    if temp is not None:
        converted = round(temp * 9/5 + 32, 2)
        label_result.config(text=f"Converted: {converted} °F")

root = tk.Tk()
root.title("Temperature Converter")

label_prompt = tk.Label(root, text="Enter the temperature:")
label_prompt.grid(row=0, column=0, padx=10, pady=10)

entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

button_convert_c = tk.Button(root, text="Convert to Celsius", command=convert_to_celsius)
button_convert_c.grid(row=1, column=0, padx=10, pady=10)

button_convert_f = tk.Button(root, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
button_convert_f.grid(row=1, column=1, padx=10, pady=10)

label_result = tk.Label(root, text="Converted: ")
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
