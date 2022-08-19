from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_x):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.setx(start_x)

    def up(self):
        self.setheading(90)
        self.forward(25)

    def down(self):
        self.setheading(270)
        self.forward(25)
