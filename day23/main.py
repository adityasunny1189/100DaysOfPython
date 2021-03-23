# with open("file.txt", mode = "a") as file:
# 	file.write("\nCGPA: 7.87")

with open("file.txt") as file:
	content = file.read()
	print(content)
	print(type(content))
	int_content = int(content)
	print(int_content)
	print(type(int_content))