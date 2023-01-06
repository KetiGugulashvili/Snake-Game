from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def final_score(self):
        self.clear()
        self.write(f"Game Over!\nFinal Score: {self.score}", align="center", font=("Arial", 30, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.final_score()
