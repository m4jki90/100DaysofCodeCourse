from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.tracer(0)
paddle1 = Paddle((-350,0))
paddle2 = Paddle((350,0))
scoreboard = Scoreboard()
ball = Ball()
screen.listen()
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce()

    if ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.defend()

    if ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.defend()

    if ball.xcor() > 360:
        ball.restart()
        scoreboard.scored1()

    if ball.xcor() < -360:
        ball.restart()
        scoreboard.scored2()







screen.exitonclick()
