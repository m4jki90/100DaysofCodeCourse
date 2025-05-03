from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.updater()

    def updater(self):
        self.goto(-80, 200)
        self.write(self.score1, align="center", font=("Courier", 80, "normal"))
        self.goto(80, 200)
        self.write(self.score2, align="center", font=("Courier", 80, "normal"))

    def scored1(self):
        self.score1 +=1
        self.clear()
        self.updater()

    def scored2(self):
        self.score2 += 1
        self.clear()
        self.updater()