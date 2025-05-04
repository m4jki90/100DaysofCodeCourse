from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars=[]
        self.create_car()

    def create_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=1,stretch_len=2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.goto(x=300,y=random.randint(-250,250))
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)











