import pandas

# data = pandas.read_csv("./csv_files/weather_data.csv")
# print(max(data["temp"].tolist()))
# print(data["temp"].max()) # series.mean median ...


# # to get a single row
# print("single row", data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()]) 

# data_dict = {
#     "students": ["a", "b", "c"],
#     "scores": [1, 2, 3]
# }

# converted_dataFrame = pandas.DataFrame(data_dict)
# converted_dataFrame.to_csv('huluuu.csv')

squirrell_data = pandas.read_csv('./csv_files/Squirrel_Census.csv')


accept_list = ["black", "red", "grey"]

new_obj = {}

new_obj["grey"] = len(squirrell_data[squirrell_data["Primary Fur Color"] == "Gray" ])
new_obj["cinnamon"] = len(squirrell_data[squirrell_data["Primary Fur Color"] == "Cinnamon" ])
new_obj["black"] = len(squirrell_data[squirrell_data["Primary Fur Color"] == "Black" ])

print(new_obj)