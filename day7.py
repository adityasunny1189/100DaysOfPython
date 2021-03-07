# Hangman game
import random

print("Hangman Game")
words_collection = ["cat", "Global Warming", "india"]
char_to_guess = words_collection[random.randint(0, len(words_collection) - 1)]
char_on_display = []
for i in char_to_guess:
	char_on_display += '_'
error_count = 0
game_not_over = True
print(char_on_display)

def print_hangman(error_count, game_not_over):
	if error_count == 1:
		print('''
			 +---------+
			 O	  |
				  |
				  |
				  |
				  |
				  |
				  |
		----------------------
		''')
	elif error_count == 2:
		print('''
			 +---------+
			 O	  |
		   	/	  |
				  |
				  |
				  |
				  |
				  |
		----------------------
		''')
	elif error_count == 3:
		print('''
			 +---------+
			 O	  |
		   	/|	  |
				  |
				  |
				  |
				  |
				  |
		----------------------
		''')
	elif error_count == 4:
		print('''
			 +---------+
			 O	  |
		   	/|\\  	  |
				  |
				  |
				  |
				  |
				  |
		----------------------
		''')
	elif error_count == 5:
		print('''
			 +---------+
			 O	  |
		   	/|\\  	  |
		   	/	  |
				  |
				  |
				  |
				  |
		----------------------
		''')
	else:
		game_not_over = False
		print('''
			 +---------+
			 O	  |
		   	/|\\  	  |
		   	/ \\  	  |
				  |
				  |
				  |
				  |
		----------------------
		''')
		print("Man Dead")
		print("GAME OVER")
	return game_not_over


while game_not_over:
	guess = input("Enter a letter: ")
	for position in range(len(char_to_guess)):
		cur_letter = char_to_guess[position]
		if guess == cur_letter:
			char_on_display[position] = guess
	print(char_on_display)
	if "_" not in char_on_display:
		game_not_over = False
		print("You Won")
	if guess not in char_to_guess:
		error_count += 1
		game_not_over = print_hangman(error_count, game_not_over)