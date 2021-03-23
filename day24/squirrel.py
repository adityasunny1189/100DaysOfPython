import pandas

data = pandas.read_csv("Data.csv")

colors = []
count = []


grey_color = data[data["Primary Fur Color"] == "Gray"]
grey_color_count = grey_color["Primary Fur Color"].count()
colors.append("Gray")
count.append(grey_color_count)

Cinnamon_color = data[data["Primary Fur Color"] == "Cinnamon"]
Cinnamon_color_count = Cinnamon_color["Primary Fur Color"].count()
colors.append("Cinnamon")
count.append(Cinnamon_color_count)

Black_color = data[data["Primary Fur Color"] == "Black"]
Black_color_count = Black_color["Primary Fur Color"].count()
colors.append("Black")
count.append(Black_color_count)


squirrel_data = {
	"colour": colors,
	"count": count
}

s_data = pandas.DataFrame(squirrel_data)
s_data.to_csv("census_count.csv")