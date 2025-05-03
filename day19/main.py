import turtle
from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red","orange","green","blue","yellow","purple"]
y_pos = [-100,-60,-20,20,60,100]
all_turtles = []

for x in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[x])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[x])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won {winner} turtle is the winner")
            else:
                print(f"You lost, {winner} turtle is the winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
