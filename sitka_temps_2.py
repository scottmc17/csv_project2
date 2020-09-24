import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
'''
print(header_row)

for index, column_header in enumerate(header_row):
    print(index,column_header)
'''

highs = []
dates = []


x = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(x)


for row in csv_file:
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2],'%Y-%m-%d' )
    dates.append(the_date)




import matplotlib.pyplot as plt 

fig = plt.figure()

plt.plot(dates, highs, c="red")

plt.title("Daily High Temp, July 2018" , fontsize=16)
plt.xlabel("")
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)

fig.autofmt_xdate()

plt.show()

