import csv 
import pandas as pd 


with open("Central_Park.csv") as filename:
    data = pd.read_csv(filename)


Gray_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinamon_count = len(data[data["Primary Fur Color"] == "Cinamon"])
Black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Primary Fur Color": ["Gray", "Cinamon", "Black"],
    "Count": [Gray_count, Cinamon_count, Black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("Done Central_Park")