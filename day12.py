# n = int(input())

# for i in range(1, n + 1):
# 	for j in range(1, n - i + 1):
# 		print(' ', end = '')
# 	for k in range(1, i + 1):
# 		print(k, end = '')
# 	print()


# for i in range(0, n + 1):
# 	for j in range(1, n - i + 1):
# 		print(n - i, end = '')
# 	print()


# for i in range(1, n + 1):
# 	for j in range(1, n-i+1):
# 		print(' ', end = '')
# 	for k in range(1, i + 1):
# 		print(i + k - 1, end = '')
# 	for l in range(i, 1, -1):
# 		print(i + l - 2, end = '')
# 	print()


# Number Guessing Game
import random
def start_game():
	print("Welcome to number guessing game")
	print("The number is between 1 and 100")
	mode = input("Enter the mode easy/hard: ")
	ans = random.randint(1, 100)
	life = 10
	if mode == "hard":
		life = 5
	print(f"You have total {life} chance")
	while life:
		guess = int(input("Enter the guessed number: "))
		life -= 1
		if ans == guess:
			print("You guessed right")
			life = 0
		elif ans > guess:
			print("Too Low")
		elif ans < guess:
			print("Too High")


start_game()
