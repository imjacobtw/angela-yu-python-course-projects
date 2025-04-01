from collections.abc import Callable
from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
CARD_CANVAS_WIDTH = 800
CARD_CANVAS_HEIGHT = 526

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
file_path = "./data/words_to_learn.csv"

try:
    open(file_path)
except FileNotFoundError:
    file_path = "./data/french_words.csv"
finally:
    flashcards = pandas.read_csv(file_path).to_dict(orient="records")

current_word_record: dict[str, str] | None = None
timer = None
flashcards_to_learn = []

def create_card_button(image: PhotoImage, callback: Callable[[], None]) -> Button:
    return Button(
        image=image,
        highlightthickness=0,
        borderwidth=0,
        activebackground=BACKGROUND_COLOR,
        command=callback
    )

def handle_wrong_button_click() -> None:
    if flashcards:
        flashcards.remove(current_word_record)
    flashcards_to_learn.append(current_word_record)
    reset()

def handle_right_button_click() -> None:
    if flashcards:
        flashcards.remove(current_word_record)
    reset()

def count_down(seconds: int) -> None:
    global timer

    if seconds > 0:
        timer = window.after(1000, count_down, seconds - 1)
    else:
        flip_card_to_back()

def flip_card_to_front() -> None:
    card_canvas.itemconfig(card_image, image=card_front_image)
    card_canvas.itemconfig(card_language_text, text="French", fill="black")
    card_canvas.itemconfig(card_word_text, text=current_word_record["French"], fill="black")

def flip_card_to_back() -> None:
    card_canvas.itemconfig(card_image, image=card_back_image)
    card_canvas.itemconfig(card_language_text, text="English", fill="white")
    card_canvas.itemconfig(card_word_text, text=current_word_record["English"], fill="white")

def reset() -> None:
    global current_word_record

    window.after_cancel("timer")

    try:
        current_word_record = random.choice(flashcards)
    except IndexError:
        save_flashcards_to_learn()
        messagebox.showinfo(
            "Session Completed!",
            "You've ran out of flashcards for this session! Come back to study later."
        )
        window.destroy()
    else:
        flip_card_to_front()
        count_down(3)

def save_flashcards_to_learn() -> None:
    words_to_learn_dataframe = pandas.DataFrame(flashcards_to_learn)
    words_to_learn_dataframe.to_csv("./data/words_to_learn.csv")

card_canvas = Canvas(width=CARD_CANVAS_WIDTH, height=CARD_CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.grid(row=0, column=0, columnspan=2)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

card_image = card_canvas.create_image(CARD_CANVAS_WIDTH // 2, CARD_CANVAS_HEIGHT // 2, image=card_front_image)
card_language_text = card_canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word_text = card_canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = create_card_button(wrong_image, handle_wrong_button_click)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = create_card_button(right_image, handle_right_button_click)
right_button.grid(row=1, column=1)

reset()

window.protocol("WM_DELETE_WINDOW", save_flashcards_to_learn)
window.mainloop()
