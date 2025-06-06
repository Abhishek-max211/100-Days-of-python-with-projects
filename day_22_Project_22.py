# Day 22
# Project-22 = The Pong Game Project
from turtle import Turtle, Screen
import time

# ────────── CONSTANTS ──────────
WIDTH, HEIGHT   = 800, 600
PADDLE_LIMIT    = 250
PADDLE_STEP     = 20
BALL_X_STEP     = 10
BALL_Y_STEP     = 10
START_SPEED     = 0.05           # seconds between frames; shrinks on paddle hit

# ────────── PADDLE ──────────
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def up(self):
        if self.ycor() < PADDLE_LIMIT:
            self.sety(self.ycor() + PADDLE_STEP)

    def down(self):
        if self.ycor() > -PADDLE_LIMIT:
            self.sety(self.ycor() - PADDLE_STEP)

# ────────── BALL ──────────
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_X_STEP
        self.y_move = BALL_Y_STEP
        self.move_speed = START_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9        # speed up each paddle hit

    def reset(self):
        self.goto(0, 0)
        self.move_speed = START_SPEED
        self.bounce_x()               # send ball toward last scorer

# ────────── SCOREBOARD ──────────
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200); self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto( 100, 200); self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self): self.l_score += 1; self.update()
    def r_point(self): self.r_score += 1; self.update()

# ────────── SCREEN SET-UP ──────────
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong – Day 22")
screen.tracer(0)

# objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball     = Ball()
score    = Scoreboard()

# controls
screen.listen()
screen.onkeypress(r_paddle.up,   "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up,   "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkey(screen.bye, "Escape")     # quick exit with Esc

# ────────── GAME LOOP ──────────
running = True
while running:
    try:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # wall bounce
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # paddle bounce
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
           (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.bounce_x()

        # miss right
        if ball.xcor() > 380:
            ball.reset()
            score.l_point()

        # miss left
        if ball.xcor() < -380:
            ball.reset()
            score.r_point()

    except Turtle.Terminator:
        # turtle graphics window was closed → stop loop
        running = False
    except Exception:
        # any other unexpected error: stop loop to avoid spam
        running = False

# optional: keep window until user clicks (only if not closed yet)
try:
    screen.exitonclick()
except Turtle.Terminator:
    pass
