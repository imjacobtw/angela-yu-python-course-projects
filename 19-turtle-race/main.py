from turtle import Screen, Turtle
import random

COLORS = ["pink", "red", "orange", "yellow", "green", "blue", "purple"]
TURTLE_STARTING_X_POSITION = -225
DISTANCE_BETWEEN_TURTLES = 30
# The number of turtles can be changed by adding more colors.
NUMBER_OF_TURTLES = len(COLORS)

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
).lower()

if user_bet not in COLORS:
    print("That turtle is not in the race. Enjoy the race anyways!")

turtles = []

for i in range(NUMBER_OF_TURTLES):
    new_turtle = Turtle()
    new_turtle.color(COLORS[i])
    new_turtle.shape("turtle")
    new_turtle.penup()

    # Calculates the starting y position of each turtle, so they are evenly spaced between each other
    # and vertically aligned on the screen.
    turtle_starting_y_position = (
        DISTANCE_BETWEEN_TURTLES
        * ((len(COLORS) // 2) + (-0.5 if len(COLORS) % 2 == 0 else 0))
    ) - (i * DISTANCE_BETWEEN_TURTLES)

    new_turtle.goto(x=TURTLE_STARTING_X_POSITION, y=turtle_starting_y_position)

    turtles.append(new_turtle)

is_game_over = False
winning_turtle_color = ""

while not is_game_over:
    for turtle in turtles:
        if not is_game_over:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

            if turtle.xcor() >= -TURTLE_STARTING_X_POSITION:
                is_game_over = True
                winning_turtle_color = turtle.pencolor()

if winning_turtle_color == user_bet:
    print(f"You've won! The {winning_turtle_color} turtle is the winner!")
else:
    print(f"You've lost! The {winning_turtle_color} turtle is the winner!")

screen.exitonclick()
