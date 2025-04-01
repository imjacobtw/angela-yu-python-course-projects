from turtle import Turtle
import random

INIT_BALL_SPEED = 5
BALL_BOUNCE_SPEED_MODIFIER = 0.1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()

    def move(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        initial_velocities = [-INIT_BALL_SPEED, INIT_BALL_SPEED]
        self.x_velocity = random.choice(initial_velocities)
        self.y_velocity = random.choice(initial_velocities)

    def bounce_y(self):
        self.y_velocity *= -1 - BALL_BOUNCE_SPEED_MODIFIER

    def bounce_x(self):
        self.x_velocity *= -1 - BALL_BOUNCE_SPEED_MODIFIER
