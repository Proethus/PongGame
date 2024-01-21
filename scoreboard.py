from turtle import *


class Scoreboard(Turtle):
    def __init__(self, player_one_score, player_two_score):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {player_one_score} : { player_two_score}", False, "center", ("Arial", 24, "normal"))

    def update_score(self, player_one_score, player_two_score):
        self.clear()
        self.write(f"Score: {player_one_score} : { player_two_score}", False, "center", ("Arial", 24, "normal"))
        self.goto(0, 260)
