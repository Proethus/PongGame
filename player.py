from turtle import *


MOVE_PACE = 40
PLAYER_START_X_POS = -350
PLAYER_START_Y_POS = 0


class Player(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.score = 0
        self.goto(player_number * PLAYER_START_X_POS, PLAYER_START_Y_POS)

    def move_up(self):
        if self.ycor() < 220:
            self.goto(self.xcor(), self.ycor() + MOVE_PACE)

    def move_down(self):
        if self.ycor() > -220:
            self.goto(self.xcor(), self.ycor() - MOVE_PACE)
