from turtle import Turtle 

class Player(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("turtle")
		self.penup()
		self.setheading(90)
		self.color("white")
		self.reset_player()

	def reset_player(self):
		self.goto(0, -280)

	def move_up(self):
		y_cor = self.ycor() + 20
		self.goto(0, y_cor)

	def move_down(self):
		y_cor = self.ycor() - 10
		self.goto(0, y_cor)
