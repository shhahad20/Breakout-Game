from turtle import Turtle
import random
weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]

Color = ["red", "green", "blue", "purple", "yellow", "pink", "cyan"]


class Wall(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(Color))
        self.goto(x=x_cor, y=y_cor)

        self.quantity = random.choice(weights)
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Walls:
    def __init__(self):
        self.y_start = 90
        self.y_end = 300
        self.walls = []
        self.create_lines()

    def create_line(self, y_cor):
        # range( start, stop, step)
        for i in range(-320, 320, 63):
            wall = Wall(i, y_cor)
            self.walls.append(wall)

    def create_lines(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_line(i)