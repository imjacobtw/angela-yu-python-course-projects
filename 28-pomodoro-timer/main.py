import tkinter

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


def count_down(count):
    global timer

    minutes = int(count // 60)
    seconds = int(count % 60)
    display_text = f"{minutes}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=display_text)

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        new_checkmark_label_text = checkmark_label.cget("text") + "✓"
        checkmark_label.config(text=new_checkmark_label_text)
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


def reset():
    global reps
    global timer

    window.after_cancel(timer)
    reps = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(width=False, height=False)

timer_label = tkinter.Label(
    text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN
)
timer_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

checkmark_label = tkinter.Label(
    text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN
)
checkmark_label.grid(column=1, row=3)

window.mainloop()
