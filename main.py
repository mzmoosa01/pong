from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

board = Screen()

board.setup(width=800, height=600)
board.title('pong')
board.bgcolor('black')
board.tracer(0)

player1 = Paddle(360)
player2 = Paddle(-360)

ball = Ball()

scoreboard = Scoreboard()

board.listen()

board.onkeypress(fun=player1.up, key='Up')
board.onkeypress(fun=player2.up, key='w')

board.onkeypress(fun=player1.down, key='Down')
board.onkeypress(fun=player2.down, key='s')

game_on = True
while game_on:
    board.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # detect collision with  paddle
    # if self.distance(paddle) < 50 and (self.xcor() > 340 or self.xcor() < -340):
    if ball.distance(player1) < 50 and ball.xcor() > 330 or ball.distance(player2) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        time.sleep(1)
        scoreboard.add_to_player2()
        print(f'player1: {scoreboard.player1_score} - player2: {scoreboard.player2_score}')

    if ball.xcor() < -380:
        ball.reset_pos()
        time.sleep(1)
        scoreboard.add_to_player1()
        print(f'player1: {scoreboard.player1_score} - player2: {scoreboard.player2_score}')


board.exitonclick()
