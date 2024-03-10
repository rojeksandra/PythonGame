from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
LEVELS = 5

class Scoreboard(Turtle):
    def __init__(self, color):
        super().__init__()
        self.level = 1
        self.color(color)
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.update_scoreboard()
        self.number_of_levels = LEVELS

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def victory(self):
        self.level = self.number_of_levels
        self.update_scoreboard()
        self.goto(0, 0)
        self.write(f"VICTORY 🏆", align=ALIGNMENT, font=FONT)







