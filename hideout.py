from turtle import Turtle
import random

HIDEOUTS = 120

class Hideout(Turtle):
    def __init__(self, color):
        super().__init__()
        self.all_hideout = []
        self.amount_hideout = HIDEOUTS
        self.color = color
        self.random_hideouts()
        self.hideturtle()


    def random_hideouts(self):
        for hideout in range(self.amount_hideout):
            hideout = Turtle("square")
            hideout.shapesize(stretch_wid=2, stretch_len=1)
            hideout.color(self.color)
            hideout.penup()
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            hideout.goto(x, y)
            self.all_hideout.append(hideout)


    def decrease_hideout(self):
        self.amount_hideout -= 30

    def reset_hideouts(self):
        for seg in self.all_hideout:
            seg.goto(10000, 10000)
