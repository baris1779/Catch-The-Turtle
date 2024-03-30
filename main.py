import time
import turtle
from random import randint

background = turtle.Screen()
background.bgcolor("PaleTurquoise1")
background.title("Catch The Turtle")

# Title
turtle.hideturtle()
turtle.penup()
turtle.setposition(0, 280)

# Timer
turtle_2 = turtle.Turtle()
turtle_2.hideturtle()
turtle_2.penup()
turtle_2.setposition(0, 260)

our_turtle = turtle.Turtle()
our_turtle.penup()
our_turtle.shape("turtle")
our_turtle.color("green")
our_turtle.turtlesize(2, 2, 2)

score = 0


def turtle_clicker(x, y):
    global score
    score = score + 1
    turtle.clear()


# Game
seconds = 20
while seconds >= 1:
    our_turtle.onclick(fun=turtle_clicker, btn=1)
    turtle.write(f"Score: {score}", font=("Verdana", 15, "normal"), align="center")
    x_s = randint(-350, 350)
    y_s = randint(-250, 250)
    our_turtle.teleport(x_s, y_s)
    turtle_2.write(f"Timer: {seconds}", font=("Verdana", 13, "normal"), align="center")
    time.sleep(0.75)
    seconds -= 1
    turtle_2.clear()

our_turtle.hideturtle()
turtle.write(f"Score: {score}", font=("Verdana", 15, "normal"), align="center")
turtle_2.write("Game Over", font=("Verdana", 13, "normal"), align="center")
turtle.mainloop()
