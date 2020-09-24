import csv
from datetime import datetime 


open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

'''
print(header_row)

for index, column_header in enumerate(header_row):
    print(index,column_header)
'''

highs = []
dates = []
lows = []


x = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(x)


for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2],'%Y-%m-%d' )
    dates.append(the_date)




import matplotlib.pyplot as plt 

fig = plt.figure()


plt.plot(dates, highs, c="red", alpha=0.5)    #add dates list to plot
plt.plot(dates, lows, c="blue", alpha=0.5)

#chart title
plt.title("High and Low Temps in 2018" , fontsize=16) #change title
plt.xlabel("", fontsize=12)

plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha=0.1)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()

