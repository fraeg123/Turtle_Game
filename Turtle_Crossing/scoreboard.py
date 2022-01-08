from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)
