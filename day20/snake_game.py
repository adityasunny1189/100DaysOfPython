from turtle import Screen
from scoreboard import ScoreBoard 
from snake import Snake
from food import Food
import time

scoreboard = ScoreBoard()
screen = Screen()
snake = Snake()
food = Food()
screen.bgcolor("black")
screen.setup(height = 600, width = 600)
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_not_over = True

while game_not_over:
	screen.update()
	time.sleep(.1)
	snake.move()

	# Collision with Food
	if snake.head.distance(food) < 15:
		food.refresh()
		scoreboard.increment()
		snake.extend()

	# Collision with Wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		scoreboard.reset()
		snake.reset()

	# Collision with Tail
	for segment in snake.segments:
		if snake.head == segment:
			continue
		if snake.head.distance(segment) < 10:
			scoreboard.reset()
			snake.reset()

screen.exitonclick()