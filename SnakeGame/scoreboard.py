
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.score=0
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score : {self.score}', align='center', font=('Courier', 20, 'normal'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, 0)

        self.write(f'Game Over', align='center', font=('Courier', 20, 'normal'))

