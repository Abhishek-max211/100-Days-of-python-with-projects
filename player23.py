from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE     = 10
FINISH_LINE_Y     = 280


class Player(Turtle):
    """Little turtle the user controls (↑ key)."""

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)          # Point up

    def move(self):
        """Step forward one MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def at_finish(self) -> bool:
        """True if the turtle has reached the top edge."""
        return self.ycor() > FINISH_LINE_Y

    def goto_start(self):
        """Put the turtle back at the starting line."""
        self.goto(STARTING_POSITION)
