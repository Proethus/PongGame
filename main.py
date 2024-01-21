import time
from turtle import *

from ball import Ball
from player import Player
from scoreboard import Scoreboard


def update_score(player):
    player.score += 1
    scoreboard.update_score(player_one.score, player_two.score)
    ball.reset_ball()
    ball.ball_speed = 0.1


def check_peddle_touched(player):
    if ball.xcor() > 320 and ball.distance(player) < 50 or ball.xcor() < -320 and ball.distance(player) < 50:
        ball.peddle_touched()
        ball.ball_speed -= 0.001


screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)
screen.title("Pong")
player_one = Player(1)
player_two = Player(-1)
ball = Ball(0.1)
scoreboard = Scoreboard(player_one.score, player_two.score)

screen.listen()
screen.onkeypress(player_one.move_up, "w")
screen.onkeypress(player_one.move_down, "s")
screen.onkeypress(player_two.move_up, "Up")
screen.onkeypress(player_two.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    check_peddle_touched(player_one)
    check_peddle_touched(player_two)

    if ball.is_wall_touched and ball.x_direction == 1:
        update_score(player_one)
    elif ball.is_wall_touched and ball.x_direction == -1:
        update_score(player_two)


screen.exitonclick()
