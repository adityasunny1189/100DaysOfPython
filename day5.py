import random

# fruits = ["Apple", "Papaya", "Kiwi"]
# for fruit in fruits:
# 	print(fruit)


# heights = [176, 173, 178, 182, 198]
# avg_height = 0
# for height in heights:
# 	avg_height += height
# print(f"Average height is: {avg_height / len(heights)}")


# Max Min Height Challange

# max_height = heights[0]
# min_height = heights[0]
# for height in heights:
# 	if max_height < height:
# 		max_height = height
# 	if min_height > height:
# 		min_height = height
# print(f"Max Height is {max_height}")
# print(f"Min height is {min_height}")

# Password Generator

length_of_password = int(input("Enter the length of password: "))
no_of_symbol = int(input("Enter the no of symbols: "))
no_of_num = int(input("Enter the no of numbers: "))
no_of_char = length_of_password - (no_of_num + no_of_symbol)
characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '<', '>', '?', '/', '[', '}', ']', '{', '|']
password = ""
while length_of_password:
	choice = random.randint(1, 3)
	if choice == 1 and no_of_symbol:
		password += symbols[random.randint(0, len(symbols) - 1)]
		no_of_symbol -= 1
		length_of_password -= 1
	elif choice == 2 and no_of_num:
		password += str(random.randint(0, 9))
		no_of_num -= 1
		length_of_password -= 1
	elif choice == 3 and no_of_char:
		password += characters[random.randint(0, len(characters) - 1)]
		no_of_char -= 1
		length_of_password -= 1
print(password)
