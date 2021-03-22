from turtle import Turtle 

class Level(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.level = 1
		self.update_screen()

	def update_screen(self):
		self.clear()
		self.goto(-300, 240)
		self.write(f"Level: {self.level}", align = "center", font = ("courier", 20, "normal"))


	def update_level(self):
		self.level += 1
		self.update_screen()

	def game_over(self):
		self.goto(0, 0)
		self.write("GAME OVER", align = "center", font = ("Arial", 25, "normal"))
