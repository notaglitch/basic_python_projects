from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Weather App")

title_label = Label(root, text="Enter a city name!")
title_label.grid(row=1, column=0, columnspan=5)

city_input = Entry(root)
city_input.grid(row=2, column=0, columnspan=5)

root.mainloop()
