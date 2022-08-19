from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.speed('fastest')
        self.hideturtle()
        self.goto(0, 260)
        self.player1_score = 0
        self.player2_score = 0
        self.write_score()

    def add_to_player1(self):
        self.player1_score += 1
        self.write_score()

    def add_to_player2(self):
        self.player2_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'{self.player2_score} - {self.player1_score}', font=('Arial', 18, 'normal'))