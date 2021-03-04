# Hangman game

char_to_guess = "Global Warming"
char_on_display = "G_o_a_ W_r_in_"
index_empty = [1, 3, 5, 8, 10, 13]


print("Hangman Game")
print(char_on_display)

game_not_over = True
error_count = 0


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


cur_index = 0

def check_new_input(word, cur_index, error_count, game_not_over):
	if char_to_guess[index_empty[cur_index]] != word:
		error_count += 1
		game_not_over = print_hangman(error_count, game_not_over)
	else:
		cur_index += 1
	return cur_index, error_count, game_not_over

while game_not_over:
	word = input("Enter the word: ")
	cur_index, error_count, game_not_over = check_new_input(word, cur_index, error_count, game_not_over)
	if cur_index == len(index_empty):
		game_not_over = False
		print("WINNER")