# Day 23
# Project-23 = The turtle Crossing Game
# Main file
import time
from turtle import Screen
from player23 import Player
from car_manager23 import CarManager
from scoreboard23 import Scoreboard

# ── Screen setup ────────────────────────────────────────────────────────────
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing – Angela Yu")
screen.tracer(0)                               # Turn off auto-refresh

# ── Game objects ────────────────────────────────────────────────────────────
player      = Player()
car_manager = CarManager()
scoreboard  = Scoreboard()

# ── Controls ────────────────────────────────────────────────────────────────
screen.listen()
screen.onkey(player.move, "Up")

# ── Main loop ───────────────────────────────────────────────────────────────
game_is_on = True
while game_is_on:
    time.sleep(0.1)          # Loop runs every 0.1 s ≈ 10 FPS
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Collision detection
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Successful crossing
    if player.at_finish():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
