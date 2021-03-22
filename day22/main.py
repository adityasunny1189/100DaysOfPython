from turtle import Screen
from player import Player 
from level import Level
from brick import Brick  
import time

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
level = Level()
brick = Brick()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_not_over = True 

while game_not_over:
	time.sleep(.3)
	screen.update()
	brick.move()

	# crossing boundary
	if player.ycor() > 300:
		player.reset_player()
		level.update_level()

	# Detect collision with bricks
	if brick.distance(player) < 40:
		level.game_over()
		game_not_over = False



screen.exitonclick()