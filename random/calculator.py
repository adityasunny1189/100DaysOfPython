from tkinter import *
from functools import partial
import math


def key_pressed(key):
    text = calculator_label.cget('text')
    text += key
    calculator_label.config(text=f"{text}")

# -------------------------------------------- Solve the Expression --------------------------------- #
# ToDo - Make more efficient


def solve_expression(num_1, op, num_2):
    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_2 - num_1
    elif op == '*':
        return num_1 * num_2
    else:
        return math.floor(num_2 / num_1)


def solve():
    num_1 = ''
    num_2 = ''
    operator = ''
    expression = calculator_label.cget('text')
    for i in expression:
        try:
            if int(i):
                num_1 += i
        except ValueError:
            operator = i
            num_2 = num_1
            num_1 = ''
    ans = solve_expression(int(num_1), operator, int(num_2))
    calculator_label.config(text=f"{ans}")


# ---------------------------------------------------------------------------------------------------- #
def reset_window():
    calculator_label.config(text='')


window = Tk()
window.config(padx=5, pady=5)
window.title("Calculator")

calculator_label = Label(text="", fg="white", height=5, width=50)
calculator_label.config(padx=10, pady=10, bg="black", font=('Arial', 12, 'normal'))
calculator_label.grid(row=0, column=0, columnspan=4)

button_1 = Button(text="1", width=10, padx=10, pady=10, command=partial(key_pressed, '1'))
button_1.grid(row=1, column=0)

button_2 = Button(text="2", width=10, padx=10, pady=10, command=partial(key_pressed, '2'))
button_2.grid(row=1, column=1)

button_3 = Button(text="3", width=10, padx=10, pady=10, command=partial(key_pressed, '3'))
button_3.grid(row=1, column=2)

button_4 = Button(text="4", width=10, padx=10, pady=10, command=partial(key_pressed, '4'))
button_4.grid(row=2, column=0)

button_5 = Button(text="5", width=10, padx=10, pady=10, command=partial(key_pressed, '5'))
button_5.grid(row=2, column=1)

button_6 = Button(text="6", width=10, padx=10, pady=10, command=partial(key_pressed, '6'))
button_6.grid(row=2, column=2)

button_7 = Button(text="7", width=10, padx=10, pady=10, command=partial(key_pressed, '7'))
button_7.grid(row=3, column=0)

button_8 = Button(text="8", width=10, padx=10, pady=10, command=partial(key_pressed, '8'))
button_8.grid(row=3, column=1)

button_9 = Button(text="9", width=10, padx=10, pady=10, command=partial(key_pressed, '9'))
button_9.grid(row=3, column=2)

button_0 = Button(text="0", width=10, padx=10, pady=10, command=partial(key_pressed, '0'))
button_0.grid(row=4, column=1)

button_plus = Button(text="+", width=10, padx=10, pady=10, command=partial(key_pressed, '+'))
button_plus.grid(row=1, column=3)

button_minus = Button(text="-", width=10, padx=10, pady=10, command=partial(key_pressed, '-'))
button_minus.grid(row=2, column=3)

button_multiply = Button(text="*", width=10, padx=10, pady=10, command=partial(key_pressed, '*'))
button_multiply.grid(row=3, column=3)

button_divide = Button(text="/", width=10, padx=10, pady=10, command=partial(key_pressed, '/'))
button_divide.grid(row=4, column=3)

button_equal = Button(text="=", width=10, padx=10, pady=10, command=solve)
button_equal.grid(row=4, column=2)

button_clear = Button(text="C", width=10, padx=10, pady=10, command=reset_window)
button_clear.grid(row=4, column=0)

window.mainloop()
