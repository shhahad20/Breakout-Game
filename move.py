from turtle import Turtle
MOVE_DIST = 50

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(0, -280)
    def Right(self):
        self.forward(MOVE_DIST)
        # self.heading()

    def Left(self):
        self.backward(MOVE_DIST)
        # self.heading()