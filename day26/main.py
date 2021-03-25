from tkinter import *

window = Tk()
window.minsize(height = 600, width = 800)
window.title("My First GUI")

def button_clicked():
	user_input_text = user_input.get()
	heading_1.config(text = user_input_text)

heading_1 = Label(text = "Heading 1", font = ("Arial", 40, "bold"))
heading_1.pack()

button = Button(text = "click me", side = "left" command = button_clicked)
button.pack()

user_input = Entry()
user_input.pack()


window.mainloop()




# def add(*args):
# 	for n in args:
# 		print(n)

# add(1,2,3)
# add(1,2,3,4,5)