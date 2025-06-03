# Day 19
# Project-19 = The turtle race Project
import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.title("Turtle Race 🐢")

# Ask user for a bet
user_bet = screen.textinput(
    title="Make your bet", 
    prompt="Which turtle will win the race? Enter a color (red, orange, yellow, green, blue, purple): "
)

# Define turtle colors and starting positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

all_turtles = []

# Create turtles
for index in range(6):
    racer = turtle.Turtle(shape="turtle")
    racer.color(colors[index])
    racer.penup()
    racer.goto(x=-250, y=y_positions[index])
    all_turtles.append(racer)

# Start the race only if user placed a valid bet
is_race_on = user_bet and user_bet.lower() in colors

if is_race_on:
    while is_race_on:
        for turtle in all_turtles:
            turtle.forward(random.randint(0, 10))
            
            # Check if turtle has crossed the finish line
            if turtle.xcor() >= 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                
                if winning_color == user_bet.lower():
                    print(f"You've WON! 🎉 The {winning_color} turtle is the winner! 🏁")
                else:
                    print(f"You've LOST. 😢 The {winning_color} turtle won the race.")
                break  # Exit the for loop once a winner is found

# Keep the window open until clicked
screen.exitonclick()
