import turtle
from player import Player
from hideout import Hideout
from enemy import Enemy
from treasure import Treasure
from scoreboard import Scoreboard
from instruction import Instruction
import random
import pygame.mixer
import time

pygame.mixer.init()
COLORS = {
    "forest": {"bg_color": "green", "image": "image/forest.gif", "sound": "sounds/forest_sound.wav", "treasure_shape": "square", "treasure_color": "yellow", "enemy_colors": ["grey"]},
    "ocean": {"bg_color": "orange", "image": "image/oceanim.gif","sound": "sounds/ocean_sound.wav", "treasure_shape": "circle", "treasure_color": "pink", "enemy_colors": ["blue"]},
    "desert": {"bg_color": "green", "image": "image/desert.gif","sound": "sounds/desert_sound.wav", "treasure_shape": "square", "treasure_color": "yellow", "enemy_colors": ["black", "yellow", "brown", "red"]}
}

collision_sound = pygame.mixer.Sound("sounds/collision.wav")
treasure_sound = pygame.mixer.Sound("sounds/tresure_sound.wav")
instruction = Instruction()

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

selected_gameboard = screen.textinput(title="Select game board", prompt="Enter the name of the gameboard: 'forest'/'ocean'/'desert'").lower()
selected_color = screen.textinput(title="Select color", prompt="Select color your turtle: 'red'/'blue'/'yellow'").lower()

player = Player()
enemy = Enemy()

if selected_gameboard not in COLORS:
    selected_gameboard = "forest"

game_data = COLORS[selected_gameboard]
screen.addshape(game_data["image"])
turtle.shape(game_data["image"])
screen.title(f"Find treasure - {selected_gameboard.capitalize()}")
gameboard_sound = pygame.mixer.Sound(game_data["sound"])
gameboard_sound.play(loops=-1)


scoreboard = Scoreboard("black" if selected_gameboard == "ocean" else "white")
hideout = Hideout(game_data["bg_color"])
treasure = Treasure(game_data["treasure_shape"], game_data["treasure_color"])



screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    player.color(selected_color if selected_color in ["red", "blue", "yellow"] else "red")

    enemy_color = random.choice(COLORS[selected_gameboard]["enemy_colors"])
    enemy.create_enemy(enemy_color)
    enemy.move()

    player_hidden = any(seg.distance(player) < 15 for seg in hideout.all_hideout)

    for element_enemies in enemy.all_enemies:
        if element_enemies.distance(player) < 12 and not player_hidden:
            print("Collision with an enemy, game over!")
            game_is_on = False
            scoreboard.game_over()
            collision_sound.play()

    if treasure.distance(player) < 15:
        treasure_sound.play()
        enemy.increase_enemies()
        enemy.speed_up()
        player.reset_player()
        hideout.reset_hideouts()
        hideout.decrease_hideout()
        hideout.random_hideouts()
        treasure.random_position_tresure()
        scoreboard.increase_level()

    if scoreboard.level > scoreboard.number_of_levels:
        game_is_on = False
        scoreboard.victory()

screen.exitonclick()
