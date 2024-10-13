import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color_column = data["Primary Fur Color"].to_list()
gray = 0
red = 0
black = 0
other = 0
for values in fur_color_column:
    if values == 'Gray':
        gray += 1
    elif values == 'Black':
        black += 1
    elif values == 'Cinnamon':
        red += 1
    else:
        other += 1
new_dict = {
      "Fur Color": ["gray", "Red", "Black"],
            "Red":  [gray, red, black]
}
color_dataframe = pandas.DataFrame(new_dict)
print(color_dataframe)
color_dataframe.to_csv("squirrel_count.csv")