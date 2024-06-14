# main.py
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Draw boundaries
boundaries = Turtle(visible=False)
boundaries.color("white")
boundaries.penup()
boundaries.goto(400, 300)
boundaries.pendown()
for _ in range(2):
    boundaries.right(90)
    boundaries.forward(600)
    boundaries.right(90)
    boundaries.forward(800)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Display temporary text prompting to press space to play
start_text = Turtle(visible=False)
start_text.color("white")
start_text.penup()
start_text.goto(0, 0)
start_text.write("Press Space to Play", align="center", font=("Courier", 24, "normal"))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = False

def start_game():
    global game_is_on
    if not game_is_on:
        game_is_on = True
        start_text.clear()  # Clear temporary text
        while game_is_on:
            screen.update()
            ball.move()

            # Detect collision with wall
            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            # Detect collision with paddle
            if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
                ball.bounce_x()
                # Adjust ball speed after hitting paddles
                ball.slow_down()
                ball.lift_acceleration()  # Add lift acceleration

            # Detect R paddle misses
            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.l_point()

            # Detect L paddle misses:
            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.r_point()

            time.sleep(ball.move_speed)  # Adjust game speed

screen.onkey(start_game, "space")

screen.exitonclick()
