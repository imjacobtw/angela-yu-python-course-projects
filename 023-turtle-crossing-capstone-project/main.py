import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars(level=scoreboard.level)

    if player.has_past_finish_line():
        scoreboard.update()
        player.reset()

    if player.is_touching_car(car_manager):
        screen.onkeypress(None, "Up")
        game_is_on = False

scoreboard.game_over()
screen.exitonclick()
