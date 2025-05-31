# Day 16
# Object Oriented Programming(OOP's)
from turtle import Turtle,Screen
timmy=Turtle()
from prettytable import PrettyTable
print(timmy)
timmy.shape("turtle")
timmy.color("blue","green")
timmy.forward(100)

# Object Attributes
my_screen=Screen()
print(my_screen.canvheight)

# Object Methods
my_screen=Screen()
my_screen.exitonclick()

# Python Packages(PyPi)
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)