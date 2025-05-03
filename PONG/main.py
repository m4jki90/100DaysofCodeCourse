from turtle import Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.tracer(0)
paddle1 = Paddle((-350,0))
paddle2 = Paddle((350,0))
ball = Ball()
screen.listen()
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce()

    if ball.distance(paddle1) or ball.distance(paddle2) < 15:
        ball.defend()






screen.exitonclick()
