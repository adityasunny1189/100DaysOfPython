from tkinter import *
import pandas
import random
# ----------------------------------------- Constants --------------------------- #

BACKGROUND_COLOR = "#B1DDC6"

try:
    word_collection_data = pandas.read_csv('data/updated_list.csv')
except FileNotFoundError:
    word_collection_data = pandas.read_csv('data/french_words.csv')
data = word_collection_data.to_dict(orient="records")
current_word = {}


def load_word():
    return random.choice(data)


def get_new_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = load_word()
    canvas.itemconfig(card_image, image=canvas_image_front)
    canvas.itemconfig(card_word, text=current_word['French'], fill='black')
    canvas.itemconfig(card_title, text='French', fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=canvas_image_back)
    canvas.itemconfig(card_word, text=current_word['English'], fill="white")
    canvas.itemconfig(card_title, text='English', fill="white")


def is_known():
    data.remove(current_word)
    updated_data = pandas.DataFrame(data)
    updated_data.to_csv('data/updated_list.csv', index=False)
    get_new_word()
# ----------------------------------------- UI Setup ----------------------------- #


window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=100, pady=100)
flip_timer = window.after(3000, flip_card)
canvas_image_front = PhotoImage(file='images/card_front.png')
canvas_image_back = PhotoImage(file='images/card_back.png')
canvas = Canvas(height=530, width=800)
card_image = canvas.create_image(400, 265, image=canvas_image_front)
card_title = canvas.create_text(400, 120, text='', font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 265, text='', font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_button_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=0)

wrong_button_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=get_new_word)
wrong_button.grid(row=1, column=1)

get_new_word()
window.mainloop()
