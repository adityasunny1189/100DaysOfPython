# Higher Lower Game
from day14 import data

def checkAns(A, B):
	if A['follower'] > B['follower']:
		return A
	return B


game_not_over = True
i = 0
score  = 0

while game_not_over:
	print("Do the compare")
	A = data[i]
	B = data[i + 1]
	print(f"A: {A['name']} from {A['country']} a {A['profession']}")
	print(f"B: {B['name']} from {B['country']} a {B['profession']}")
	guess = input("Enter Your Choice: ")
	guessAns = B
	if guess == "A":
		guessAns = A
	ans = checkAns(A, B)
	if guessAns['follower'] == ans['follower']:
		score += 1
		i += 1
		print(f"Your current score is {score}")
	else:
		game_not_over = False
		print("Sorry Game Over")
