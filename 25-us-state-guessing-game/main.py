import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.color("black")
writer.penup()
writer.hideturtle()

states_data = pandas.read_csv("50_states.csv")
states_dict = states_data.to_dict()

player_score = 0
guessed_states = []

while player_score != 50:
    answer_state = screen.textinput(
        title=f"{player_score}/50 States Correct", prompt="What's another state's name?"
    )

    if not answer_state:
        continue

    answer_state = answer_state.title()

    if answer_state == "Exit":
        missing_states = []

        for state in states_dict["state"].values():
            if state not in guessed_states:
                missing_states.append(state)

        missing_states_dataframe = pandas.DataFrame(missing_states)
        missing_states_dataframe.to_csv("states_to_learn.csv")
        break

    for state_index, state_name in states_dict["state"].items():
        if state_name == answer_state and state_name not in guessed_states:
            player_score += 1
            guessed_states.append(state_name)
            state_x_coord = states_dict["x"][state_index]
            state_y_coord = states_dict["y"][state_index]
            writer.goto(state_x_coord, state_y_coord)
            writer.write(state_name, align="center", font=("Arial", 10, "normal"))

writer.goto(0, 300)
game_over_text = (
    "You guessed all 50 states!"
    if player_score == 50
    else "You should study your U.S. geography!"
)
writer.write(game_over_text, align="center", font=("Arial", 20, "normal"))

screen.exitonclick()
