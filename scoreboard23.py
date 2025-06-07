from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """Displays the current level and Game Over message."""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update()

    def update(self):
        """Refresh the level display."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Advance to the next level."""
        self.level += 1
        self.update()

    def game_over(self):
        """Show Game Over in the centre of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
