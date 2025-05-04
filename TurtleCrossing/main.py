import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
counter = 0
while game_is_on:
    counter += 1
    time.sleep(0.1)
    screen.update()
    car_manager.move()
    if counter % 6 == 0:
        car_manager.create_car()

    for car in car_manager.cars:
        if car.distance(player)<15:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300:
        player.starting()
        car_manager.speed_up()
        scoreboard.refresh()


screen.exitonclick()
