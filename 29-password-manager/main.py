from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

letters = [
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
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not (website and username and password):
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it okay to save?",
    )

    if not is_ok:
        return
    
    with open("data.txt", "a") as file:
        file.write(f"{website} | {username} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()
    pyperclip.copy(password)


def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_characters = [choice(letters) for _ in range(nr_letters)]
    password_characters.extend([choice(symbols) for _ in range(nr_symbols)])
    password_characters.extend([choice(numbers) for _ in range(nr_numbers)])

    shuffle(password_characters)
    password = "".join(password_characters)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


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

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky=EW)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky=E)

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky=EW)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=E)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=EW)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=EW)

window.mainloop()
