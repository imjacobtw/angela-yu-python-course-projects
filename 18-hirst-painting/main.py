from turtle import Screen, Turtle
import random

# import colorgram
#
# extracted_colors = colorgram.extract('image.jpg', 20)
# rgb_colors = []
#
# for color in extracted_colors:
#     rgb_colors.append((
#         color.rgb.r,
#         color.rgb.g,
#         color.rgb.b,
#     ))
#
# print(rgb_colors)


COLOR_LIST = [
    (156, 118, 71),
    (200, 162, 84),
    (151, 3, 84),
    (101, 26, 18),
    (154, 54, 73),
    (61, 85, 63),
    (236, 203, 95),
    (46, 156, 180),
    (9, 49, 88),
    (1, 69, 159),
    (157, 212, 187),
    (129, 137, 70),
    (168, 113, 90),
    (240, 242, 246),
    (212, 49, 66),
    (106, 35, 27),
    (25, 83, 152),
]
DOT_SIZE = 20
NUMBER_OF_ROWS = 10
NUMBER_OF_COLUMNS = 10
SPACE_BETWEEN_DOTS = 50

painting_width = DOT_SIZE + SPACE_BETWEEN_DOTS * (NUMBER_OF_COLUMNS - 1)
painting_height = DOT_SIZE + SPACE_BETWEEN_DOTS * (NUMBER_OF_ROWS - 1)

starting_x_position = -(painting_width / 2) + DOT_SIZE
starting_y_position = -(painting_height / 2) + DOT_SIZE

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.penup()
turtle.speed("fastest")
turtle.setpos(starting_x_position, starting_y_position)

for x in range(NUMBER_OF_COLUMNS):
    for y in range(NUMBER_OF_ROWS):
        color = random.choice(COLOR_LIST)
        turtle.dot(DOT_SIZE, color)
        turtle.forward(SPACE_BETWEEN_DOTS)

    turtle.backward(SPACE_BETWEEN_DOTS)
    turtle_x = turtle.pos()[0]
    turtle_y = turtle.pos()[1]
    turtle.setpos(turtle_x, turtle_y + SPACE_BETWEEN_DOTS)
    heading = 180 if turtle.heading() == 0 else 0
    turtle.setheading(heading)

turtle.hideturtle()

screen.exitonclick()
