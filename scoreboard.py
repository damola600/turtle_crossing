from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.speed("fastest")
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Level = {self.level}", move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
