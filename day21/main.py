from turtle import Screen
from board import Board 
from ball import Ball 
from scoreboard import Scoreboard 
import time

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

p1 = Board((350, 0))
p2 = Board((-350, 0))
pong = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(p1.move_up, "Up")
screen.onkey(p1.move_down, "Down")
screen.onkey(p2.move_up, "w")
screen.onkey(p2.move_down, "s")

game_not_over = True 

while game_not_over:
	time.sleep(pong.ball_speed)
	screen.update()
	pong.move()

	# Ball Collision with top and bottom wall
	if pong.ycor() > 280 or pong.ycor() < -280:
		pong.bounce()

	# Detect Collision with board
	if pong.distance(p1) < 50 and pong.xcor() > 320 or pong.distance(p2) < 50 and pong.xcor() < -320:
		pong.board_bounce()

	# Detect Ball missed the board
	if pong.xcor() > 380:
		pong.reset()
		scoreboard.p2_point()

	if pong.xcor() < -380:
		pong.reset()
		scoreboard.p1_point()



screen.exitonclick()