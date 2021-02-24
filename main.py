from turtle import Turtle, Screen
from ball import Ball
import time
import random


screen = Screen()
timmy = Turtle()
ball = Ball()
count = 0
x_pos = [5, 25, 50, 100, 150, 200, 250, 350, 400, -5, -25, -50, -100, -150, -200, -250, -350]
y_pos = [0, 25, 50, 100, 150, 200, 250]

# ****************** Board Turtle ********************** #
screen.listen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.title("The Breakout")
timmy.color("white")
timmy.shape('square')
timmy.shapesize(stretch_wid=1, stretch_len=6)
timmy.penup()
timmy.goto(x=0, y=-240)

# **************************** many turtles start ***************************** #
allturtle = []

for i in range(20):
    turtle = Turtle()
    turtle.shape('square')
    turtle.color("white")
    turtle.penup()
    turtle.shapesize(stretch_wid=1, stretch_len=6)
    turtle.goto(x=random.choice(x_pos), y=random.choice(y_pos))
    allturtle.append(turtle)

# **************************** many turtles end ***************************** #

orange = Turtle()
orange.color("white")
orange.goto(x=0, y=-240)


def left():
    timmy.forward(-20)


def right():
    timmy.forward(20)


screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")

# ****************** Ball turtle ********************* #
game = True
while game:
    time.sleep(0.1)
    ball.ball_moves()
    if ball.ycor() > 290:
        ball.bounce_for_y()

    elif ball.xcor() < -370 or ball.xcor() > 370:
        ball.bounce_for_x()

    if ball.ycor() < -270:
        game = False
        print("gameover")
        break

    if ball.distance(timmy) < 25 or ball.distance(timmy) < 35 and ball.ycor() < -240:
        print("madecon")
        ball.bounce_for_y()

    for brick in allturtle:
        if ball.distance(brick) < 10:
            print('colissio')
            count += 1
            print(count)








screen.exitonclick()