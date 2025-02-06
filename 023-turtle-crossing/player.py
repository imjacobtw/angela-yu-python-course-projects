from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def has_past_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)

    def is_touching_car(self, car_manager):
        for car in car_manager.cars:
            if self.distance(car) < 20:
                return True

        return False
