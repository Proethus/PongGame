import time
from turtle import *


class Ball(Turtle):
    def __init__(self, ball_speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.fillcolor("white")
        self.penup()
        self.x_direction = 1
        self.y_direction = 1
        self.direction_changed = False
        self.is_wall_touched = False
        self.ball_speed = ball_speed

    def move(self):
        new_y = self.ycor() + 10 * self.y_direction
        if self.ycor() == 280:
            self.y_direction = -1
        elif self.ycor() == -280:
            self.y_direction = 1

        new_x = self.xcor() + 10 * self.x_direction
        self.goto(new_x, new_y)
        if abs(self.xcor()) > 360:
            time.sleep(1)
            self.is_wall_touched = True

    def peddle_touched(self):
        if not self.direction_changed:
            self.x_direction = -1 * self.x_direction
            self.direction_changed = True
        else:
            self.direction_changed = False

    def reset_ball(self):
        self.goto(0, 0)
        time.sleep(2)
        self.direction_changed = False
        self.is_wall_touched = False
        self.x_direction = self.x_direction * -1
