# Day 18
from turtle import Turtle,Screen
timmy_the_turtle=Turtle()
# Shape of the turtle
timmy_the_turtle.shape("turtle")
# Change the Color of the turtle
timmy_the_turtle.color("blue","green")
# Draw a square by turtle
def square():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)
    
for item in range(1,5):
    square()
# Draw a dashed line
for item in range(0,15):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.pendown()
# Draw the shapes using turtle
def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
for shape_side_n in range(3,11):
    draw_shape(shape_side_n) 
screen=Screen()
screen.exitonclick()
# Tuple in Python
my_tuple=(1,4,8)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])