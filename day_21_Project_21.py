# Project-21 = The Snake Game Project By using Class Inheritance
from turtle import Screen, Turtle
import time, random

STEP = 20  # distance snake moves each frame

# ---------------- SNAKE (list of segments) ---------------- #
class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            t = Turtle('square')
            t.color('white')
            t.penup()
            t.goto(-i * STEP, 0)
            self.segments.append(t)
        self.head = self.segments[0]

    # movement & growth
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(STEP)

    def grow(self):
        t = Turtle('square')
        t.color('white')
        t.penup()
        t.goto(self.segments[-1].pos())
        self.segments.append(t)

    # direction controls
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

# ----------------- FOOD (inherits Turtle) -------------- #
class Food(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.penup()
        self.color('yellow')
        self.shapesize(0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

# --------------- SCOREBOARD (inherits Turtle) ----------- #
class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.color('white')
        self.score = 0
        self.goto(0, 260)
        self.show()

    def show(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 24, 'normal'))

    def increase(self):
        self.score += 1
        self.show()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 24, 'bold'))

# -------------------- MAIN GAME ------------------------ #

def main():
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor('black')
    screen.title('Simple Snake')
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    running = True
    while running:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Eat food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.grow()
            score.increase()

        # Hit wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            score.game_over()
            running = False

        # Hit tail
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                score.game_over()
                running = False

    screen.exitonclick()

if __name__ == '__main__':
    main()
