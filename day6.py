# def my_function():
# 	print("Inside the custom function")
# 	print("Another line")

# my_function()

# num = 0
# while num < 10:
# 	num += 1
# 	print(num)

def I(a):
	a += 1
	return a

a = 5
while a < 10:
	a = I(a)
	print(a)
print(f"outer a {a}")