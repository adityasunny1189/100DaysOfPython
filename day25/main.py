# numbers = [1, 2, 3, 4, 5]
# num_list = [num + 1 for num in numbers]
# print(num_list)

# name = "Aditya"
# letters = [letter for letter in name]
# print(letters)

# new_list = [num * 2 for num in range(1, 5)]
# print(new_list)

# even_list = [num for num in range(1, 20) if num % 2 == 0]
# print(even_list)


# var1 = open("file1.txt")
# var2 = open("file2.txt")
# list1 = var1.readlines()
# list2 = var2.readlines()
# print(list1)
# print(list2)
# new_list = [int(num) for num in list1 if num in list2]
# print(new_list)
# var1.close()
# var2.close()

# Iterate over pandas dataframe

import pandas

student_df = pandas.DataFrame({
		"Students": ["Amit", "Aditya", "Srikant", "Adarsh"],
		"score": [90, 87, 67, 96]
	})

for (index, row) in student_df.iterrows():
	if row.Students == "Aditya":
		print(row.score)