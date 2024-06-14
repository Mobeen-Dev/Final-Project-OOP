# ball.py
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)  # Slightly increased size
        self.shape("circle")
        self.penup()
        self.x_move = 1  # Decreased initial speed
        self.y_move = 1  # Decreased initial speed
        self.move_speed = 0.01  # Adjusted move speed

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01  # Adjusted move speed
        self.bounce_x()

    def slow_down(self):
        self.move_speed *= 0.9  # Adjusted move speed

    def lift_acceleration(self):
        if self.y_move > 0:
            self.y_move += 0.1
        else:
            self.y_move -= 0.1
