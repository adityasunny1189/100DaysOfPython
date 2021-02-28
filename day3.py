height_of_user = int(input("Enter your height: "))
if height_of_user > 120:
	print("Can Ride")
	age = int(input("Enter your age: "))
	if age <= 12: 
		print("Your fair is: 7rs")
	elif age > 12 and age <= 18:
		print("Your fair is: 10rs")
	else:
		print("Your fair is: 15rs")
else:
	print("Can't ride")


# Challange 1

num = int(input("Enter a number: "))
if num % 2 == 0:
	print("Even number")
else:
	print("Odd number")

Challange 2

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print("It's a leap year")
else:
	print("It not a leap year")


# Love Calculator Challange

your_name = input("Enter your name: ")
crush_name = input("Enter her name: ")
true_count = 0
love_count = 0
for alphabet in your_name:
	if alphabet == 't' or alphabet == 'r' or alphabet == 'u' or alphabet == 'e':
		true_count += 1
	if alphabet == 'l' or alphabet == 'o' or alphabet == 'v' or alphabet == 'e':
		love_count += 1

for alphabet in crush_name:
	if alphabet == 't' or alphabet == 'r' or alphabet == 'u' or alphabet == 'e':
		true_count += 1
	if alphabet == 'l' or alphabet == 'o' or alphabet == 'v' or alphabet == 'e':
		love_count += 1	

true_love = str(true_count) + str(love_count)
print(f"True Love is {true_love}")