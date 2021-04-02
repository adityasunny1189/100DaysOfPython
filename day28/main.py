from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    length_of_password = 10
    no_of_symbol = 3
    no_of_num = 3
    no_of_char = length_of_password - (no_of_num + no_of_symbol)
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '<', '>', '?', '/', '[', '}', ']', '{', '|']
    password = ""
    while length_of_password:
        choice = random.randint(1, 3)
        if choice == 1 and no_of_symbol:
            password += symbols[random.randint(0, len(symbols) - 1)]
            no_of_symbol -= 1
            length_of_password -= 1
        elif choice == 2 and no_of_num:
            password += str(random.randint(0, 9))
            no_of_num -= 1
            length_of_password -= 1
        elif choice == 3 and no_of_char:
            password += characters[random.randint(0, len(characters) - 1)]
            no_of_char -= 1
            length_of_password -= 1
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def reset_window():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) < 3:
        messagebox.showinfo(title=website, message="Please check the website entered")
    elif len(password) < 6:
        messagebox.showinfo(title=password, message="Your Password length is too short")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}\nConfirm Details")
        if is_ok:
            with open('data.txt', mode='a') as file:
                file.write(f"\n{website}\t{email}\t{password}")
            reset_window()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100, pady=50)
window.title("Password Manager")

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "adityasunny1189@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="generate password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
