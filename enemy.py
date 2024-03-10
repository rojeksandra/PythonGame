from turtle import Turtle
import random

ENEMY_DISTANCE_MOVE = 10
FREQUENCY_OF_ENEMIES = 14


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_enemies = []
        self.freq_enemies = FREQUENCY_OF_ENEMIES
        self.speed = ENEMY_DISTANCE_MOVE


    def create_enemy(self,color):
        # too many cars, we must decrease freq
        random_chance = random.randint(1, self.freq_enemies)
        if random_chance == 1:
            new_enemy = Turtle("circle")
            new_enemy.penup()
            new_enemy.color(color)
            new_enemy.goto(x=280, y=random.randint(-260, 280))
            new_enemy.setheading(180)
            self.all_enemies.append(new_enemy)


    def increase_enemies(self):
        self.freq_enemies -= 3

    def move(self):
        for car in self.all_enemies:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += 2


