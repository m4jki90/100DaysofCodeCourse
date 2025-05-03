import random
import turtle as t

color_list = [(202, 164, 110),(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def row():
    for x in range(10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

def new_row():
    tim.penup()
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)
    tim.pendown()

for y in range(10):
    row()
    new_row()

t.Screen()
t.exitonclick()