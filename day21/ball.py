from turtle import Turtle 

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.color("white")
		self.x_move = 10
		self.y_move = 10
		self.ball_speed = 0.1

	def move(self):
		x_cor = self.xcor() + self.x_move
		y_cor = self.ycor() + self.y_move
		self.goto(x_cor, y_cor)

	def bounce(self):
		self.y_move *= -1

	def board_bounce(self):
		self.x_move *= -1
		self.ball_speed *= .9
		if self.ball_speed < .0729:
			self.color("red")

	def reset(self):
		self.goto(0, 0)
		self.ball_speed = 0.1
		self.board_bounce()
