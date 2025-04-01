import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = tkinter.PhotoImage(file="./images/false.png")
        self.false_button = tkinter.Button(
            image=false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        true_image = tkinter.PhotoImage(file="./images/true.png")
        self.true_button = tkinter.Button(
            image=true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        self.canvas.config(bg=("green" if is_right else "red"))
        self.window.after(1000, self.get_next_question)
