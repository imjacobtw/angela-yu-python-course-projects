from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def handle_add_button_click() -> None:
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not (website and username and password):
        messagebox.showinfo(
            title="Oops", 
            message="Please don't leave any fields empty!"
        )
        return

    has_user_clicked_okay = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it okay to save?",
    )

    if not has_user_clicked_okay:
        return

    new_entry = {website: {"email": username, "password": password}}

    try:
        with open("data.json", "r") as file:
            entries = json.load(file)
            entries.update(new_entry)
    except FileNotFoundError:
        entries = new_entry
    finally:
        with open("data.json", "w") as file:
            json.dump(entries, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
    pyperclip.copy(password)


def handle_generate_password_button_click() -> None:
    number_of_letters = randint(8, 10)
    number_of_symbols = randint(2, 4)
    number_of_numbers = randint(2, 4)

    password_characters = [choice(LETTERS) for _ in range(number_of_letters)]
    password_characters.extend([choice(SYMBOLS) for _ in range(number_of_symbols)])
    password_characters.extend([choice(NUMBERS) for _ in range(number_of_numbers)])

    shuffle(password_characters)
    password = "".join(password_characters)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


def handle_search_button_click() -> None:
    try:
        website = website_entry.get()
        
        with open("data.json", "r") as file:
            entries = json.load(file)
        
        if website in entries:
            title = website
            username = entries[website]["email"]
            password = entries[website]["password"]
            message = f"Email: {username}\nPassword: {password}"
        else:
            title = "Error"
            message = "No details exist for that website."
    except FileNotFoundError:
        title = "Error"
        message = "No Data File Found."
    finally:
        messagebox.showinfo(
            title=title, 
            message=message
        )


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(width=False, height=False)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=E)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky=EW)
website_entry.focus()

search_button = Button(text="Search", command=handle_search_button_click)
search_button.grid(row=1, column=2, sticky=EW)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky=E)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=E)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=EW)

generate_password_button = Button(text="Generate Password", command=handle_generate_password_button_click)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=handle_add_button_click)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
