from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITION = (-280, -280)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_player()

    def up(self):
        self.setheading(UP)
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        self.setheading(DOWN)
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def right(self):
        self.setheading(RIGHT)
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def left(self):
        self.setheading(LEFT)
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def reset_player(self):
        self.goto(START_POSITION)


