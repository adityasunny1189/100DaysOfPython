from turtle import Turtle 

POSITIONS = [(380, -40), (380, -20), (380, 40), (380, 20)]

class Brick(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("square")
		self.shapesize(1, 3)
		self.color("white")
		self.penup()
		self.x_cor = 380
		self.update_screen()

	def update_screen(self):
		self.clear()
		self.goto(self.x_cor, 0)

	def move(self):
		self.x_cor = self.xcor() - 10
		self.update_screen()
