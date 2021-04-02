from tkinter import *

window = Tk()
window.title("Mile to Kilometer")
window.config(padx = 20, pady = 20)

def calculate():
	kilo_dis = int(mile_input.get()) * 2
	kilo_label.config(text = f"{kilo_dis}")

mile_input = Entry()
mile_input.config(width = 10)
mile_input.grid(row = 0, column = 1)

mile_label = Label(text = "Miles")
mile_label.grid(row = 1, column = 2)

equal_label = Label(text = "is equal")
equal_label.grid(row = 1, column = 0)

kilo_dis = 0
kilo_label = Label(text = f"{kilo_dis}")
kilo_label.grid(row = 1, column = 1)

k_label = Label(text = "kilos")
k_label.grid(row = 1, column = 2)

calc_button = Button(text = "calculate", command = calculate)
calc_button.grid(row = 2, column = 1)


window.mainloop()