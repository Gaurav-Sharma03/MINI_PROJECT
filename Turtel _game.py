import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.title("Turtle Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the player (turtle)
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)
player.setposition(0, 0)

# Create the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.setposition(random.randint(-250, 250), random.randint(-250, 250))

# Variables to track the score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))

# Functions to move the player
def move_up():
    y = player.ycor()
    player.sety(y + 20)

def move_down():
    y = player.ycor()
    player.sety(y - 20)

def move_left():
    x = player.xcor()
    player.setx(x - 20)

def move_right():
    x = player.xcor()
    player.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while True:
    # Check if player has collected the food
    if player.distance(food) < 20:
        # Move the food to a new random position
        food.setposition(random.randint(-250, 250), random.randint(-250, 250))
        # Update the score
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 14, "normal"))

    screen.update()
