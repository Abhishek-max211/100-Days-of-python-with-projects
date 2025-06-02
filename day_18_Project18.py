# Project-18 = The Hirst Painting Project
import turtle as t
import random

# Setup the screen and turtle
t.colormode(255)  # Set RGB color mode
tim = t.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

# Define a color palette (you can also extract from an image using colorgram)
color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243),
    (149, 75, 50), (223, 201, 135), (52, 93, 124),
    (172, 154, 40), (138, 31, 20), (134, 163, 184),
    (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165),
    (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89),
    (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153)
]

# Set starting position
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# Draw dots
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

# Exit on click
screen = t.Screen()
screen.exitonclick()
