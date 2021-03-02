import random

# print(random.randint(1, 10))

# float_num = random.random() * 10

# print(float_num)

# list_items = ['python', 'java', 'c++']

# print(list_items)

# new_string = "Hello how are you"

# new_string_list = new_string.split()

# print(new_string_list)

# print(new_string_list[random.randint(0, len(new_string_list) - 1)])

# Challange 1

# row1 = ["_", "_", "_"]
# row2 = ["_", "_", "_"]
# row3 = ["_", "_", "_"]

# matrix = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")

# index = input("Enter the index: ")

# index1 = int(index[0]) - 1
# index2 = int(index[1]) - 1

# matrix[index1][index2] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# Rock Paper Scissor

rock = "Rock".lower()
paper = "Paper".lower()
scissor = "Scissor".lower()

choices = [rock, paper, scissor]

your_choice = input("Enter Your Choice: ")
comp_choice = choices[random.randint(0,2)]

print(your_choice)
print(comp_choice)

if your_choice == comp_choice:
	print("Match Draw")
elif (your_choice == rock and comp_choice == paper) or (your_choice == paper and comp_choice == scissor) or (your_choice == scissor and comp_choice == rock):
	print("You lose")
else:
	print("You Win")