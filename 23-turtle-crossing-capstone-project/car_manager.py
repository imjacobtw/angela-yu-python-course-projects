import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 15
CAR_MAX_Y = 250
CAR_MIN_Y = -250
CAR_MAX_X = 320
CAR_MIN_X = -320


class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(NUMBER_OF_CARS):
            self.create_car()

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        color = random.choice(COLORS)
        new_car.color(color)
        starting_x = random.randint(CAR_MIN_X, CAR_MAX_X)
        starting_y = random.randint(CAR_MIN_Y, CAR_MAX_Y)
        new_car.goto(starting_x, starting_y)
        self.cars.append(new_car)

    def move_cars(self, level):
        for car in self.cars:
            if car.xcor() < CAR_MIN_X:
                new_x = random.randint(CAR_MAX_X, CAR_MAX_X + 50)
                new_y = random.randint(CAR_MIN_Y, CAR_MAX_Y)
            else:
                new_x = car.xcor() - (
                    STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * (level - 1))
                )
                new_y = car.ycor()

            car.goto(new_x, new_y)
