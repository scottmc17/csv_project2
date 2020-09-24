import csv
from datetime import datetime 


open_file = open("death_valley_2018_simple.csv", "r")

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


#x = datetime.strptime('2018-07-01', '%Y-%m-%d')  #example
#print(x)


for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2],'%Y-%m-%d' )
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)     #append date to list




import matplotlib.pyplot as plt 

fig = plt.figure()


plt.plot(dates, highs, c="red", alpha=0.5)    #add dates list to plot
plt.plot(dates, lows, c="blue", alpha=0.5)

#chart title
plt.title("Daily High and Low temperatures - 2018\nDeath Valley" , fontsize=16) #change title
plt.xlabel("", fontsize=12)

plt.fill_between(dates, highs, lows, facecolor= 'blue', alpha=0.1)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", labelsize=12)

fig.autofmt_xdate()

plt.show()

