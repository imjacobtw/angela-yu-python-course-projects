from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_x):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(init_x, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 260:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -260:
            self.goto(self.xcor(), new_y)
