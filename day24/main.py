# with open("weather_data.csv") as file:
# 	weather_data = file.readlines()
# 	print(weather_data)


# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temperatures = []
# 	for row in data:
# 		if row[1] != 'temp':
# 			temperatures.append(int(row[1]))
# 	print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

# mean_temp = data["temp"].mean()
# max_temp = data.temp.max()
# print(f"Mean Temp: {mean_temp}")
# print(f"Max Temp: {max_temp}")

# days_list = data.day 
# print(days_list)

# Get The Row with max temp
# print(data[data.temp == data.temp.max()])

data_dict = {
	"students": ["Aditya", "Amit", "Adarsh", "Motu"],
	"cgpa": [7.87, 9.18, 8.98, 8.2]
}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("students_report.csv")