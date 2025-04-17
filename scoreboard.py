from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.level=1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-280, y=260)
        self.write(arg=f"Level:{self.level}", align="left", font=FONT)

    def score_increase(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=-70,y=0)
        self.write(arg="Game Over",font=FONT)








