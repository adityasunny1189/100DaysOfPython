# num = int(input())
# power = int(input())

# if power == 0:
# 	num = 1
# else:
# 	for i in range(1, power + 1):
# 		num *= num

# print(num)

# n = int(input())

# for i in range(n):
# 	for j in range(n):
# 		print(n, end = '')
# 	print()

# char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# n = int(input())

# for i in range(1, n + 1):
# 	for j in range(1, i + 1):
# 		print(char[j - 1], end = '')
# 	print()

# n = int(input())

# for i in range(1, n + 1):
# 	for j in range(1, i + 1):
# 		print(i - j, end = ''
# 	print()

# n = int(input())

# for i in range(1, n + 1):
# 	for j in range(1, i + 1):
# 		print(char[i-j-1], end = '')
# 	print()

# Calculator

def calculator(num1, num2, operation):
	if operation == "+":
		return (num1 + num2)
	elif operation == "-":
		return (num1 - num2)
	elif operation == "*":
		return (num1 * num2)
	else:
		return (num1 / num2)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
choice = input("+\n-\n*\n/\nChoice: ")
continue_calculating = True

while continue_calculating:
	result = calculator(num1, num2, choice)
	continue_operation = input(f"{num1} {choice} {num2} is {result}, do you want to continue: ")
	if continue_operation == "no":
		print(result)
		continue_calculating = False
	else:
		num1 = result
		num2 = int(input("Enter a number: "))
		choice = input("+\n-\n*\n/\nChoice: ")

