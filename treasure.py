from turtle import Turtle
import random


class Treasure(Turtle):
    def __init__(self, shape, color):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.color(color)
        self.random_position_tresure()

    def random_position_tresure(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)



