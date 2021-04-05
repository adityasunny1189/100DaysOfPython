import requests
from tkinter import *


def get_quote():
    response = requests.get(url="http://api.kanye.rest")
    response_data = response.json()
    return response_data['quote']


def next_quote():
    new_quote = get_quote()
    canvas.itemconfig(kanye_quote, text=new_quote)


window = Tk()
window.title("Kanye Quotes")

canvas = Canvas(height=500, width=500)
quote = get_quote()
kanye_quote = canvas.create_text(250, 250, text=quote)
canvas.grid(row=0, column=0, columnspan=2)

new_quote_button = Button(text="Next", command=next_quote)
new_quote_button.grid(row=1, column=0)

window.mainloop()
