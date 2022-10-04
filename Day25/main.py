# with open("weather_data.csv") as filename:
#     data = filename.readlines()
#     print(data)

import csv 

with open("weather_data.csv") as filename:
    data = csv.reader(filename)
    temperature = []

    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)